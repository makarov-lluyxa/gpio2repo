import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
foto = 6
GPIO.setup(foto, GPIO.IN)
while True:
    GPIO.output(led, not GPIO.input(foto))
