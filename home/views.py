from ast import Return
from tkinter import Place
from django.shortcuts import render
from .models import banks, hospitals, malls, places , restraunts , libraries , toilets
from django.http import JsonResponse
import json

def index(request) :
    return render(request , 'index.html')

def search(request) :
    return render(request , 'search.html')

def search_result(request) :
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            data = places.objects.filter(Name__icontains=query) 
            return render(request, 'search_result.html', {'places':data , 'query':query  })
        else:
            print("No information to show")
            return render(request, 'search_result.html', {})

def login(request) :
    return render(request , 'login.html')

def register(request) :
    return render(request , 'register.html')

def restraunt(request) :
    data = list(restraunts.objects.values())
    return JsonResponse(data , safe=False)

def librarie(request) :
    data = list(libraries.objects.values())
    return JsonResponse(data , safe=False)

def toilet(request) :
    data = list(toilets.objects.values())
    return JsonResponse(data , safe=False)

def bank(request) :
    data = list(banks.objects.values())
    return JsonResponse(data , safe=False)

def hospital(request) :
    data = list(hospitals.objects.values())
    return JsonResponse(data , safe=False)

def mall(request) :
    data = list(malls.objects.values())
    return JsonResponse(data , safe=False)