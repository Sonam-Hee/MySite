from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact


# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('this is homepage')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('this is aboutpage')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse('this is servicepage')

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        detail=request.POST.get('detail')
        contact=Contact(name=name, email=email, phone=phone, detail=detail)
        contact.save()
    return render(request, 'contact.html')
    #return HttpResponse('this is contactpage')