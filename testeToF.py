from machine import I2C,Pin
from time import sleep
from vl53l0x import *
import _thread

S1Shut = Pin(23, Pin.OUT)
S2Shut = Pin(19, Pin.OUT)
S3Shut = Pin(18, Pin.OUT)
S1Shut.value(0)
S2Shut.value(0)
S3Shut.value(0)


#set up buses and objects
i2c=I2C(0, scl=Pin(22),sda=Pin(21)) #declare i2c bus

#for each VL53L0X in turn, set the XSHUT high (i.e. turn it on)
#initialise it with a new object (which will use the default i2c address
#and THEN use the object's set_address method to chnage the i2c address for 2 of the sensors
#(the third sensor can just use the default address)

S1Shut.value(1)
sleep(0.1)
FrontSensor = VL53L0X(i2c)
FrontSensor.set_address(32)
sleep(0.1)
S2Shut.value(1)
LeftSensor = VL53L0X(i2c)
LeftSensor.set_address(31)
S3Shut.value(1)
sleep(0.1)
RightSensor = VL53L0X(i2c)

left = 0
right = 0
front = 0

def _sensor_left(counter=5,time=0.02):
    val = 0
    global left
    c = 0 
    while 1:
        val += round(LeftSensor.range())
        c += 1
        if c >= counter:
            left = val/5
            counter = 0
            val = 0
            sleep(time)

def _sensor_right(counter=5,time=0.02):
    val = 0
    global right
    c = 0 
    while 1:
        val += round(RightSensor.range())
        c += 1
        if c >= counter:
            right = val/5
            counter = 0
            val = 0
            sleep(time)

def _sensor_front(counter=5,time=0.02):
    val = 0
    global front
    c = 0 
    while 1:
        val += round(FrontSensor.range())
        c += 1
        if c >= counter:
            front = val/5
            counter = 0
            val = 0
            sleep(time)
            

_thread.start_new_thread(_sensor_left,())
_thread.start_new_thread(_sensor_right,())
_thread.start_new_thread(_sensor_front,())
while 1:
    sleep(0.5)
    print("range do sensor:")
    print(left)
    print(right)
    print(front)
    
    
