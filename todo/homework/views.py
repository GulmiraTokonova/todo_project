from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def newf(request):
    return HttpResponse("WElCOME TO THE APP TODO-ADMIN")
def homepage(request):
    return render(request,"index.html")
def homework(request):
    return render(request,"homework.html")