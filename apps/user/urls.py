from django.conf.urls import url
from apps.user import views

urlpatterns = [
    url(r'^logincheck/$', views.logincheck),
    url(r'^index/$', views.index),
    url(r'^$', views.logincheck)
]
