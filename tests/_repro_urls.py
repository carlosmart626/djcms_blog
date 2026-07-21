from django.contrib import admin
from django.urls import path
from tests.urls import urlpatterns as base

urlpatterns = [path('admin/', admin.site.urls)] + list(base)
