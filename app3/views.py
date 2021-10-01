from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test2fun(request):
    return HttpResponse('hello world')
def loginfun(request):
    return render(request,'login.html')
