from django.conf.urls import url, include

urlpatterns = [
    url(r'v1/', include('api.v1.urls', namespace='v1'))
]
