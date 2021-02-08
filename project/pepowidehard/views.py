from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"main.html")
def galery_view(request):
    return render(request,"galery.html")
def data_view(request):
    return render(request,"data.html")
def htag(request):
    return render(request,"main.html")
