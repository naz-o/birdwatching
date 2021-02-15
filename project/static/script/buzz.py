from gpiozero import Buzzer
buzzer = Buzzer(17)


def buzz():
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)
