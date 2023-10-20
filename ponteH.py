from machine import PWM, Pin


class L298N:
    def __init__(self, f_left,b_left,f_right,b_right):
        self.f_left = Pin(f_left)
        self.b_left = Pin(b_left)
        self.f_right = Pin(f_right)
        self.b_right = Pin(b_right)
        
        
        self.forward_left = PWM(self.f_left,freq=2000, duty=0)
        self.forward_right = PWM(self.f_right,freq=2000, duty=0)
        self.backward_left = PWM(self.b_left,freq=2000, duty=0)
        self.backward_right = PWM(self.b_right,freq=2000, duty=0)
    
    def _forward(self, val = 1023):
        self.forward_left = PWM(self.f_left,freq=2000,duty=val)
        self.forward_right = PWM(self.f_right,freq=2000,duty=val)
        self.backward_left = PWM(self.b_left,freq=2000, duty=0)
        self.backward_right = PWM(self.b_right,freq=2000, duty=0)
    
    def _backward(self, val = 1023):
        self.forward_left = PWM(self.f_left,freq=2000,duty=0)
        self.forward_right = PWM(self.f_right,freq=2000,duty=0)
        self.backward_left = PWM(self.b_left,freq=2000,duty=1023)
        self.backward_right = PWM(self.b_right,freq=2000,duty=1023)
    
    def _right(self,r=1023,l=512):
        self.forward_left = PWM(self.f_left,freq=2000,duty=l)
        self.forward_right = PWM(self.f_right,freq=2000,duty=r)
        self.backward_left = PWM(self.b_left,freq=2000,duty=0)
        self.backward_right = PWM(self.b_right,freq=2000,duty=0)
    
    def _left(self,r=512,l=1023):
        self.forward_left = PWM(self.f_left,freq=2000,duty=l)
        self.forward_right = PWM(self.f_right,freq=2000,duty=r)
        self.backward_left = PWM(self.b_left,freq=2000,duty=0)
        self.backward_right = PWM(self.b_right,freq=2000,duty=0)

    def _stop(self):
        self.forward_left = PWM(self.f_left,freq=2000,duty=0)
        self.forward_right = PWM(self.f_right,freq=2000,duty=0)
        self.backward_left = PWM(self.b_left,freq=2000,duty=0)
        self.backward_right = PWM(self.b_right,freq=2000, duty=0)