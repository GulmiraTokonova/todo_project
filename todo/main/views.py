from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"ind.html")

def test(request):
    return render(request,"test.html")