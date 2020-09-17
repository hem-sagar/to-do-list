from django.conf.urls import url
from . import views

urlpatterns = [
    url('',views.home, name="home"),
    url('delete/<list_id>', views.delete, name="delete"),
    url('cross_off/<list_id>', views.cross_off, name="cross_off"),
    url('uncross/<list_id>', views.uncross, name="uncross"),
]
