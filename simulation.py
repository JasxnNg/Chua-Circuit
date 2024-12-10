# import vpython


# import time 
import math
import matplotlib.pyplot as plt
import numpy as np
import sys

def func(x):
    # return x / r2 
    return -1 * math.atan(x) * math.e ** (-1 * x)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

dt = 0.01

t = 0
vals = input("Do you want to use default values? (T/F): ")
if vals == "T":
    x = 0.3
    y = 0
    z = 0 
    alpha = 15.6
    beta = 28
elif vals == "F": 
    x = float(input("Input x: "))
    y = float(input("Input y: "))
    z = float(input("Input z: "))

    alpha  = float(input("Input alpha: "))
    beta   = float(input("Input beta: "))
else: 
    raise Exception(f"You entered: {vals}, which is not one of T/F")
x_arr = []
y_arr = []
z_arr = []
limit = sys.float_info.max / 1e3
first = -1.143;
second = -0.714;
while t < 50 or x >  limit or y > limit or z > limit:
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

 

    h = second * x + 0.5 * (first - second) * (abs(x + 1) - abs(x - 1))

    xdot = alpha * (y - x - h)
    ydot = x - y + z
    zdot  = - beta * y

    x += xdot * dt
    y += ydot * dt
    z += zdot * dt
    # if t % 1 < 0.015:
    x_arr.append(x)
    y_arr.append(y)
    z_arr.append(z)
    
    # print(x, y, z, t)
        # print(xdot, ydot, zdot)
    
    t += dt
ax.plot(x_arr, y_arr, z_arr,label='parametric curve')
plt.show()


