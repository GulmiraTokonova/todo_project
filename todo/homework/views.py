
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import ToMeet,Habits


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


def habits(request):
    habits_list = Habits.objects.all()
    return render(request, "habits.html", {"habits_list": habits_list})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom= Habits()
        tom.name = request.POST.get("name")
        tom.comment= request.POST.get("comment")
        tom.done_for_today= request.POST.get("done_for_today")
        tom.important= request.POST.get("important")
        tom.save()
    return HttpResponseRedirect("/")


# def add_habits(request):
#     form = request.POST
#     text = form["name"]
#     habits = Habits(name = text)
#     habits.save()
#     return redirect(habits)