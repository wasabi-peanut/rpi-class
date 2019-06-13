# import many libraries
from __future__ import print_function
import datetime
from DS1621 import *
import smbus

def main():
    i2c_1 = smbus.SMBus(1)
    read_degreesC_byte(i2c_1,0x4f)      #wake it up and wait for a bit
    time.sleep(0.6)

    try:                                              #read the temperature from the DS1621
        temp = read_degreesC_hiRes_oneshot(i2c_1, 0x4f)
    except:
        temp = "Failed to read temperature"
    print (temp)

if __name__ == '__main__':
    main()

