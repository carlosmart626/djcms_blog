from django.conf import settings


DJ_BLOG_DEFAULT_URL = getattr(
    settings,
    'DJ_BLOG_DEFAULT_URL',
    None)

DJ_BLOG_CACHE_TIME = getattr(
    settings,
    'DJ_BLOG_CACHE_TIME',
    60*60*24)
