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


"""SIH17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from sih17.views import PredictionsView, LoginView, logout, SignupView, demographics, pipeline, education, team, login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/', include('api.urls', namespace='api')),
    url(r'^$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^employment/$', PredictionsView.as_view(), name='employment'),
    url(r'^demographics/$', demographics, name='demographics'),
    url(r'^about_us/$', pipeline, name='pipeline'),
    url(r'^education/$', education, name='education'),
    url(r'^team/$', team, name='team')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
