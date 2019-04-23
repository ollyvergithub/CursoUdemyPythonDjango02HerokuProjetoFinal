from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    #import pdb; pdb.set_trace()
    print("Estou aqui")
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return redirect('home')
