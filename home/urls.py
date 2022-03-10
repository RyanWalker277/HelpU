from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path('', views.index , name='index' ),
    path('search', views.search , name='search' ),
    path('search_result', views.search_result , name='search_result' ),
    path('login', views.login , name='login' ),
    path('register', views.register , name='register' ),
    path('json', views.json , name='json' ),
]
