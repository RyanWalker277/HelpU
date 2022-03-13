from ast import Return
from email import message
from pydoc import importfile
from tkinter import Place
from django.shortcuts import redirect, render
from .models import banks, hospitals, malls, restraunts, libraries, toilets
from django.http import JsonResponse
import json
from django.views.generic import View
from .form import *
from django.contrib.auth.models import auth
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def search(request):
    return render(request, 'search.html')


def search_result(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            data = malls.objects.filter(Name__icontains=query)  
            return render(request, 'search_result.html', {'places': data, 'query': query})
        else:
            print("No information to show")
            return render(request, 'search_result.html', {})


def login(request):
    return render(request, 'login.html')

def restraunt(request):
    data = list(restraunts.objects.values())
    return JsonResponse(data, safe=False)


def librarie(request):
    data = list(libraries.objects.values())
    return JsonResponse(data, safe=False)


def toilet(request):
    data = list(toilets.objects.values())
    return JsonResponse(data, safe=False)


def bank(request):
    data = list(banks.objects.values())
    return JsonResponse(data, safe=False)


def hospital(request):
    data = list(hospitals.objects.values())
    return JsonResponse(data, safe=False)


def mall(request):
    data = list(malls.objects.values())
    return JsonResponse(data, safe=False)


class signupview(View):
    def get(self, request):
        fm = SignupForm()
        return render(request, 'register.html', {'form': fm})

    def post(self, request):
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request , "Registration Successful!")
            return redirect('/register')
        else:
            return render(request, 'register.html', {'form': fm})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request , user)
            return redirect("/")

        else:
            messages.info(request , "invalid credentials")
            return redirect("login")
    else:
        return render(request, 'login.html')

def results(request):
    return render(request, 'results.html')
