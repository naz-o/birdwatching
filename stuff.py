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
from bruh import StreamingOutput, StreamingServer
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
print("deebug")
pir = MotionSensor(18)
dhtDevice = adafruit_dht.DHT22(board.D2)

#camera rotation falls die cam upside down fotografiert
camera.rotation = 180

def start_camera():
    camera.start_preview()


def stop_camera():
    camera.stop_preview()
    #exit the program
    exit()

#take photo when motion is detected
def takephoto():
    global i
    try:
        print(i)
        i = int(i)
        i = i +1
        file = open("test.txt","w")
        file.write(str(i))
        file.close()
    except:
        i = 1
        file = open("test.txt","w")
        file.write(str(i))
        file.close()

    camera.capture('./project/media/posts/image%s.jpg' % i)
    dbobject.bild = 'posts/image{}.jpg'.format(i)
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
            print("Debug 1")
            sleep(2)
        except RuntimeError as error:
            print("Debug 2")
            sleep(1)
            print(error)
            continue
    avg = sum(temperatureA)/len(temperatureA)
    dbobject.temperature = str(avg)
    avg2 = sum(humidityA)/len(humidityA)
    dbobject.humidity = str(avg2)
    dbobject.datum = datetime.datetime.now()
    dbobject.save()
    print("Saved data the id is{}".format(str(dbobject.id)))
    print("The average Temperature is", round(avg,2))
    print("The average Humidity is", round(avg2,2))
    print('A photo has been taken')
    sleep(5)
    print("Debug 3")
#assign a function that runs when motion is detected

#    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
    #    print(error.args[0])
    #    time.sleep(2.0)
    #    continue

camera = picamera.PiCamera(resolution='640x480', framerate=24)
output = StreamingOutput()
camera.start_recording(output, format='mjpeg')
address = ('', 8000)
server = StreamingServer(address, StreamingHandler)
server.serve_forever()


while True:
    pir.wait_for_motion()
<<<<<<< HEAD
    print("Waiting for motion sensor to activate:")
    camera.stop_recording()
    takephoto()
    camera.start_recording()
=======
    takephoto()
>>>>>>> 0c6144001508b7765c9f4fb84d6acbd93103a2d5
