from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),  # potentiall use path, following tutorial and pretty sure this is an outdated method
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
