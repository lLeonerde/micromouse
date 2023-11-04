from ponteH import L298N
from time import sleep
h = L298N(26,25,32,33)

h._backward()
print('andando pra frente')
sleep(0.5)
print('parando')
h._stop()
