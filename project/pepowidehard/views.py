from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import djangodb
"""
from gpiozero import Buzzer
from time import sleep
buzzer = Buzzer(17)
"""

all = djangodb.objects.all()
data= {
    "data": all
}
realtimehumidity = "15"
realtimetemperature = "69"
dview = {
    "humidity": realtimehumidity,
    "temperature": realtimetemperature
}

def index(request):
    return render(request,"main.html")
def galery_view(request):
    return render(request,"galery.html",data)
def data_view(request):
    return render(request,"data.html",dview)
def htag(request):
    return render(request,"main.html")
    """
def buzzer_button(request):
    print("buzzer ist on")
    print(str(request))
    #buzzer.on()
    sleep(1)
    #buzzer.off()
    print("buzzer ist off")
    return render(request,"main.html")
    """
