from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import djangodb
from random import randint
#import board
#import adafruit_dht
#dhtDevice = adafruit_dht.DHT22(board.D2)
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
    "data": all
}
current = {
    "humidity": realtimehumidity,
    "temperature": realtimetemperature,
    "data": all
}
def index(request):
    return render(request,"main.html",current)
def galery_view(request):
    return render(request,"galery.html",data)
def data_view(request):
    return render(request,"data.html",dview)
def htag(request):
    return render(request,"main.html")
def getdatatemp(request):
    #temperature = dhtDevice.temperature
    return HttpResponse(str(randint(0,20)) + "C")
def getdatahum(request):
    #humidity = dhtDevice.humidity
    return HttpResponse(str(randint(0,100)) + "%")

def buzzer_button(request):
   # buzzer.on()
    print("Buzzer on")
    #sleep(1)
    #buzzer.off()
    return HttpResponse("Did the buzzer lmao")