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
]