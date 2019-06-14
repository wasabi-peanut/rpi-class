import socket
import RPi.GPIO as GPIO
from motor import *


#Motor(IN1,IN2,PWM,STANDBY,(Reverse polarity?))
right = Motor(14,15,18,23,False)
left = Motor(25,8,7,23,False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("localhost", 7778))
sock.listen(1)

connection, client_address = sock.accept()
print("client connected:" + str(client_address))
try:
    while True:
        data = connection.recv(10)
        if data:
            data = data.split("|")
            speed_right = data[0]*100
            speed_left  = data[1]*100
            beep_beep  = data[2]

            right.drive(speed_right)
            left.drive(speed_left)

            if (beep_beep):
                GPIO.output(4, 1)
            else:
                GPIO.output(4, 0)

        else:
            break
finally:
    connection.close
