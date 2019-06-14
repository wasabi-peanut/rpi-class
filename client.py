import RPi.GPIO as GPIO
import socket
from gpiozero import MCP3008
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = 'IP GOES HERE'
server_port = 7778
sock.connect((server_ip, server_port))


GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN)



right = MCP3008(channel=1)
left = MCP3008(channel=0)


data = "0|0|0"
while 1:
    newdata = str(right.value) + "|" + str(left.value) + "|" + str(GPIO.input(12))
    if (newdata != data):
        data = newdata
        sock.sendall(data)
     
