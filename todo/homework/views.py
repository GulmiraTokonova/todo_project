from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import ToMeet
# Create your views here.
def newf(request):
    return HttpResponse("WElCOME TO THE APP TODO-ADMIN")
def homepage(request):
    return render(request,"index.html")
def homework(request):
    return render(request,"homework.html")
def meeting(request):
    tomeet_list=ToMeet.objects.all()
    return render(request,"meeting.html",{"tomeet_list":tomeet_list})

    

def add_tomeet(request):
    form = request.POST
    text = form["tomeet_text"]
    tomeet = ToMeet(persone = text)
    tomeet.save()
    return redirect(meeting)