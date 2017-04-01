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

from sih17.views import PredictionsView, LoginView, logout, SignupView, demographics

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'api/', include('api.urls', namespace='api')),
                  url(r'^predictions/$', PredictionsView.as_view(), name='predictions'),
                  url(r'^$', LoginView.as_view(), name='login'),
                  url(r'^logout/$', logout, name='logout'),
                  url(r'^signup/', SignupView.as_view(), name='signup'),
                  url(r'^demographics/$', demographics, name='demographics')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)