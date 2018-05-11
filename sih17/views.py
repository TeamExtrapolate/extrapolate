# Copyright 2018 Team Extrapolate Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import uuid
from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from analysis.forms import AnalysisTestForm
from analysis.script import execute
from django.utils.decorators import method_decorator
from api.tasks import upload_s3
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.shortcuts import resolve_url
from django.contrib.sites.shortcuts import get_current_site
from .decorators import ajax_login_required, redirect_predictions
from django.contrib.auth.decorators import login_required
from user.forms import UserCreateForm

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


class SuccessURLAllowedHostsMixin:
    success_url_allowed_hosts = set()

    def get_success_url_allowed_hosts(self):
        allowed_hosts = {self.request.get_host()}
        allowed_hosts.update(self.success_url_allowed_hosts)
        return allowed_hosts


class SignupView(FormView):
    form_class = UserCreateForm
    template_name = 'authentication/signup.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')


def login(request):
    return redirect('employment')


class LoginView(SuccessURLAllowedHostsMixin, FormView):
    """
    Display the login form and handle the login action.
    """
    form_class = AuthenticationForm
    authentication_form = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'authentication/login.html'
    redirect_authenticated_user = False
    extra_context = None

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    @method_decorator(redirect_predictions)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        """Ensure the user-originating redirection URL is safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            return resolve_url(settings.LOGIN_REDIRECT_URL)
        return redirect_to

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        url = self.get_success_url()
        response = {
            "login": True,
            "redirect": url
        }
        return JsonResponse(data=response, status=200)

    def form_invalid(self, form):
        return JsonResponse(data={'error': form.errors}, status=422)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_success_url(),
            'site': current_site,
            'site_name': current_site.name,
        })
        if self.extra_context is not None:
            context.update(self.extra_context)
        return context


def logout(request):
    auth_logout(request)
    return redirect('login')


def demographics(request):
    return render(request, 'demographics.html')


class PredictionsView(FormView):
    """
        View to handle and run machine learning model
    """
    template_name = 'employment.html'
    form_class = AnalysisTestForm

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_exempt)
    @method_decorator(ajax_login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        file = self.request.FILES['test_file']
        old_path = 'tmp/tests/%s.xlsx' % uuid.uuid4()
        with open(old_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        data = execute(old_path)
        path = data[-1]
        upload_s3.apply_async([old_path, path, self.request.user.email, data[0]],
                              queue='uploads',
                              routing_key='s3.uploads')
        if os.path.exists(path):
            with open(path, 'rb') as fh:
                response = HttpResponse(fh.read(),
                                        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                response['Content-Disposition'] = 'inline; filename=' + \
                    os.path.basename(path)
                return response

    def form_invalid(self, form):
        return JsonResponse(data={'error': form.errors}, status=422)


def pipeline(request):
    return render(request, "pipeline.html")


def education(request):
    return render(request, "education.html")


def team(request):
    return render(request, "team.html")
