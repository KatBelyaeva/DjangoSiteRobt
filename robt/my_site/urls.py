from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('price', price, name='price'),
    path('review', review, name='review'),
    path('blog', my_blog, name='my_blog'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
