from django.conf.urls import url
from apps.jixiao import views

urlpatterns = [
    url(r'^ceshi/$', views.ceshi),
    url(r'^index/$', views.index, name='index'),
    url(r'^mingxi/(?P<userid>\d+)/(?P<year>\d+)/(?P<mon>\d+)/$',views.mingxi, name='mingxi')
]
