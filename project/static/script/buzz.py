
from gpiozero import Buzzer
from time import sleep
import os
buzzer = Buzzer(17)

def buzzer_button():
    print("buzzer ist on")
    buzzer.on()
    sleep(1)
    buzzer.off()
    print("buzzer ist off")
    os.system("echo hurensohnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
buzzer_button()
