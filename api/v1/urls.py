from django.conf.urls import url

from .views import LoginView, TestLoginView, analysis_post

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login-v1'),
    url(r'test/$', TestLoginView.as_view(), name='test-v1'),
    url(r'^post-analysis/$', analysis_post, name='post-analysis-v1'),
]
