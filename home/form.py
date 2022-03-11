from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label = "Password" , widget=forms.PasswordInput(attrs={'class':'w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline'}))
    password2 = forms.CharField(label = "Confirm Password" , widget=forms.PasswordInput(attrs={'class':'w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline'}))
    email = forms.CharField(required=True , widget=forms.EmailInput(attrs={'class':'w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline'}))
    class Meta:
        model = User
        fields = {'email' , 'username'}
        #fields = {'username' , 'email'}
        widgets = {'username':forms.TextInput(attrs={'class':'w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline'})}