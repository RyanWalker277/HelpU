import imp
from django.contrib import admin
from django.urls import path , include
from home import views
from .views import *

urlpatterns = [
    path('', views.index , name='index' ),
    path('search', views.search , name='search' ),
    path('search_result', views.search_result , name='search_result' ),
    path('login', views.login , name='login' ),
    path('register', signupview.as_view() , name='register' ),
    path('restraunts', views.restraunt , name='restraunts' ),
    path('toilets', views.toilet , name='toilets' ),
    path('libraries', views.librarie , name='libraries' ),
    path('malls', views.mall , name='restraunts' ),
    path('banks', views.bank , name='toilets' ),
    path('hospitals', views.hospital , name='libraries' ),
    path('results', views.results , name='results' ),
]
