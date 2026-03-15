from django.shortcuts import render,redirect

def index_method(request):
    return render(request,'main/index.html')

def about_method(request):
    return render(request,'main/about.html')


