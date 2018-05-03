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

from django.http import JsonResponse
from django.shortcuts import redirect


def ajax_login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.method == "POST" and request.is_ajax() and not request.user.is_authenticated:
            return JsonResponse(data={'error': 'authentication required'}, status=401)
        return func(request, *args, **kwargs)

    return wrapper


def redirect_predictions(func):
    def wrapper(request, *args, **kwargs):
        if request.method == "GET" and request.user.is_authenticated:
            return redirect('predictions')
        return func(request, *args, **kwargs)

    return wrapper
