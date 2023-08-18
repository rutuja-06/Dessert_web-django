from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1': "this is sent",
        'variable2':"this is rj"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
   # return HttpResponse("this is services page")

def cake(request):
    return render(request, 'cake.html')
   # return HttpResponse("this is cake page")

def cookies(request):
    return render(request, 'cookies.html')
   # return HttpResponse("this is cake page")

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")  # ignored
    return render(request, 'contact.html')
   # return HttpResponse("this is contact page")