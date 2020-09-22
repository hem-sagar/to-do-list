from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.home, name="home"),
    #url(r'^delete/<id>/', views.delete, name="delete"),
    path(r'delete/<int:list_id>', views.delete, name="delete"),
    path(r'cross_off/<int:list_id>', views.cross_off, name="cross_off"),
    path(r'uncross/<int:list_id>', views.uncross, name="uncross"),
    path(r'edit/<int:list_id>', views.edit, name="edit"),
]
