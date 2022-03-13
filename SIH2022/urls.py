from difflib import IS_CHARACTER_JUNK
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('search', include('home.urls')),
    path('search_result', include('home.urls')),
    path('login', include('home.urls')),
    path('register', include('home.urls')),
    path('json', include('home.urls')),
    path('restraunts', include('home.urls')),
    path('toilets', include('home.urls')),
    path('libraries', include('home.urls')),
    path('malls', include('home.urls')),
    path('hospitals', include('home.urls')),
    path('banks', include('home.urls')),
    path('results', include('home.urls')),
]