from django.conf.urls import url, include
from django.contrib import admin
from todo_list import views
from django.urls import path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('',include('todo_list.urls')),
]
