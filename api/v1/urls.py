from django.conf.urls import url

from api.v1.views import StockView

urlpatterns = [
    url(r'^stocks/$', StockView.as_view(), name='stocks')
]
