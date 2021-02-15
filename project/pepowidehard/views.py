from django.shortcuts import render
from django.http import HttpResponse
from .models import djangodb
from gpiozero import Buzzer

buzzer = Buzzer(17)
all = djangodb.objects.all()
data= {
    "data": all
}
def index(request):
    return render(request,"main.html")
def galery_view(request):
    return render(request,"galery.html",data)
def data_view(request):
    return render(request,"data.html")
def htag(request):
    return render(request,"main.html")
def buzzing(request):
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
    return render(request,"main.html")
print("bruh")
