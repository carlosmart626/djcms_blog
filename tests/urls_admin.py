#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""URLconf that adds the admin site, used by admin rendering tests."""
from django.contrib import admin
from django.urls import include, path

from tests.urls import urlpatterns as base_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
] + list(base_urlpatterns)

__all__ = ['urlpatterns', 'include']
