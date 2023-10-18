from machine import PWM, Pin
from time import sleep

class L298N:
    def __init__(self, pin_forward, pin_backward):
        self.forward = PWM(Pin(pin_forward),freq=20000, duty=0)
        self.backward = PWM(Pin(pin_backward),freq=2000, duty=0)
        self.speed = 0
    
    def forward(self, val = 1023):
        self.speed = val
        self.backward.duty = 0
        self.forward.duty = val
        
    def backward(self, val = 1023):
        self.speed = -val
        self.forward.duty = 0
        self.backward.duty = 1023


        
