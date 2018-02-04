from django.shortcuts import render

def home(request):
    return render(request, 'oodlums/home.html')

def contact(request):
    return render(request, 'oodlums/contact.html')
