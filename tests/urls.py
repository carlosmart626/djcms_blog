from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.urls import include, re_path

from djcms_blog.sitemaps import PostsSitemap

sitemaps = {
    'blog': PostsSitemap,
}

urlpatterns = [
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap-xml'),
]

urlpatterns += i18n_patterns(
    re_path(r'^', include('djcms_blog.urls')),
)
