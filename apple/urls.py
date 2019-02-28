from django.conf.urls import url
from apple.views import test

urlpatterns = [
    url(r"^api/test/$", test, name="wallet-register")
]