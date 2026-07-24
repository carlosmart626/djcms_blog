"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from djcms_blog.sitemaps import PostsSitemap

sitemaps = {
    'blog': PostsSitemap,
}

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

urlpatterns += i18n_patterns(
    re_path(r'^', include('djcms_blog.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
    urlpatterns = [
        re_path(r'^static/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
