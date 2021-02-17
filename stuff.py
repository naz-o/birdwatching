#import the necessary packages
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
import datetime
import board
import adafruit_dht
# Example to find average of list
import os
import sys
import django
sys.path.append(
    os.path.join(os.path.dirname(__file__), 'project')
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pepowide.settings")
django.setup()
from django.conf import settings


from pepowidehard.models import djangodb




#GPIO17 #11 Buzzer
#GPIO18 #12 PIR
#GPIO2 #3 Temperature and Humidity
dbobject =  djangodb()
camera = PiCamera()
pir = MotionSensor(18)
dhtDevice = adafruit_dht.DHT22(board.D2)

#camera rotation falls die cam upside down fotografiert
camera.rotation = 180

def start_camera():
    camera.start_preview()

#image image names
i = 0


def stop_camera():
    camera.stop_preview()
    #exit the program
    exit()

#take photo when motion is detected
def takephoto():
    global i
    i = i + 1
    camera.capture('/extdrive/image%s.jpg' % i)
    camera.capture('/project/media/posts/image%s.jpg' % i)
    djangodb.bild = '/project/media/posts/image%s.jpg' % i
    a = 0
    temperatureA=[]
    humidityA=[]
    while a < 3:
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            temperatureA.append(temperature_c)
            humidityA.append(humidity)
            a = a + 1
            sleep(2)
        except RuntimeError as error:
            sleep(1)
            print(error)
            continue
    avg = sum(temperatureA)/len(temperatureA)
    dbobject.temperature = str(avg)
    avg2 = sum(humidityA)/len(humidityA)
    dbobject.humidity = str(avg2)
    print("The average Temperature is", round(avg,2))
    print("The average Humidity is", round(avg2,2))
    print('A photo has been taken')
    sleep(5)

#assign a function that runs when motion is detected

#    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
    #    print(error.args[0])
    #    time.sleep(2.0)
    #    continue
while True:
    pir.wait_for_motion()
    takephoto()
