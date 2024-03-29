from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import djangodb
from random import randint
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT22(board.D2)

from gpiozero import Buzzer
from time import sleep
buzzer = Buzzer(17)

all = djangodb.objects.all()
data= {
    "data": list(all)
}
dview = {
    "data": all[:20]
}
current = {
    "data": all,
    "latestpicture": djangodb.objects.last(),
}
def index(request):
    return render(request,"main.html",current)
def galery_view(request):
    data={"data":djangodb.objects.all()}
    return render(request,"galery.html",data)
def data_view(request):
    return render(request,"data.html",dview)
def htag(request):
    return render(request,"main.html")
def getdatatemp(request):
    temperature = dhtDevice.temperature
    return HttpResponse("Temperature: "+str(temperature) + "C")
def getdatahum(request):
    humidity = dhtDevice.humidity
    return HttpResponse("Humidity: "+ str(humidity) + "%")
def buzzer_button(request):
    buzzer.on()
    print("Buzzer on")
    sleep(1)
    buzzer.off()
    return HttpResponse("Did the buzzer lmao")
def getdatatempavg(request):
    templist = list(all.values_list("temperature",flat=True)[:5])
    templistint=[]
    i = 0
    for x in templist:
        templistint.append(float(x))
    tempsum = sum(templistint)
    tempvg=int(tempsum)/len(templistint)
    return HttpResponse("Temperature: "+str(tempvg)+"C")
def getdatahumavg(request):
    humlist = list(all.values_list("humidity",flat=True)[:5])
    humlistint=[]
    i = 0
    for x in humlist:
        humlistint.append(float(x))
    humsum = sum(humlistint)
    humavg=int(humsum)/len(humlistint)
    return HttpResponse("Humidity: "+str(humavg)+"%")
def getbirdswatched(request):
    listcount = len(list(all.values_list()))
    return HttpResponse("Birds watched: "+str(listcount))
