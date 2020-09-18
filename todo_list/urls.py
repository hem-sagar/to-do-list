from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^',views.home, name="home"),
    url(r'^delete/(?P<pk>.*)', views.delete, name="delete"),
    url(r'^cross_off/(?P<pk>.*)', views.cross_off, name="cross_off"),
    url(r'^uncross/(?P<pk>.*)', views.uncross, name="uncross"),
    url(r'^edit/(?P<pk>.*)', views.edit, name="edit"),
]
