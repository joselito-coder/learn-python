from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context = {
        "variable":" This is mai beriable",
        "var2":"this is variable 2"
    }
    
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')


def services(request):
    # return HttpResponse("this is services page")
    return render(request,'services.html')


def contact(request):
    # return HttpResponse("this is contact page")
    return render(request,'contact.html')
