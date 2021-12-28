from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# from django.contrib.messages import constants as messages
from django.contrib import messages



# Create your views here.

def index(request):
    context = {
        "variable":" This is mai beriable",
        "var2":"this is variable 2"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(name=name, email=email, phone=phone,desc=desc,date=date)
        contact.save()
        messages.success(request, 'Your message has been sent.')

    return render(request,'contact.html')
