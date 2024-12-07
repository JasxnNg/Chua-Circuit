# import vpython


# import time 
import math
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    # return x / r2 
    return -1 * math.atan(x) * math.e ** (-1 * x)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

dt = 0.01
# x = 0.05
# y = 1e-7
# alpha = 0.0001
# beta = 0.05
# r1 = 2.6
# r2 = 1e6
# z = 1e-9
# c2 = 1e-5
t = 0
x = 0.3
y = 0
z = 0

alpha  = 15.6;
beta   = 28; 
m0     = -1.143;
m1     = -0.714;
x_arr = []
y_arr = []
z_arr = []
while t < 100:
    # dx = alpha * (y - x - func(x))
    # dy = (x - y + r1 * z) / (r2 * c2)
    # dz = -1 * beta * y

    # x += dx * dt
    # y += dy * dt
    # z += dz * dt
    # t += dt
    # if t % 2 < 0.0015: 
    #     ax.scatter(x, y, z) 
    #     print(x, y, z, t)

 

    h = m1 * x + 0.5 * (m0-m1)* (abs(x+1) -abs(x-1));

    xdot = alpha*(y-x-h);
    ydot = x - y+ z;
    zdot  = -beta*y;

    x += xdot * dt
    y += ydot * dt
    z += zdot * dt
    # if t % 1 < 0.015:
    x_arr.append(x)
    y_arr.append(y)
    z_arr.append(z)
    
    print(x, y, z, t)
        # print(xdot, ydot, zdot)
    
    t += dt
ax.plot(x_arr, y_arr, z_arr,label='parametric curve')
plt.show()


#g1 = graph()
#g2 = graph()
#g3 = graph()
#m0 = -1.143;
#m1 = -0.714;
#x_1 = 0.3
#y_1 = 0
#z_1 = 0
#alpha  = 15.6;
#beta   = 28;
#
#def conversion_function(x):
#    h = m1 * x + 0.5 * (m0-m1)* (abs(x+1) -abs(x-1))
#    
#    
#while True: 