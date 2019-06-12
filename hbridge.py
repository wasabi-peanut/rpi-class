from motor import *
from time import sleep #Only used for example

#Motor(IN1,IN2,PWM,STANDBY,(Reverse polarity?))
test = Motor(14,15,18,23,False)

test.drive(100) #Forward 100% dutycycle
sleep(1)
