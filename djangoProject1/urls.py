from django.contrib import admin
from django.urls import path

import main
from main import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', views.post_list, name ='post_list'),
]
