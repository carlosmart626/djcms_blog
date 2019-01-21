from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('djcms_blog.urls')),
]
