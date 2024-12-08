
import time
import math
import sys
import matplotlib.pyplot as plt

val = math.sqrt(3)
def random(modulo = 1):
    seed = time.time()
    x = seed % 1
    y = seed % 1 * 97e4 / 7
    z = seed % 1 * 3e4
    alpha = seed * 3e4 % 1 * 7
    beta = seed % 1 * 51e4

    t = 0
    dt = 0.01

    m0 = -1.143;
    m1 = -0.714;
    while t < 50:

 
        h = m1 * x + 0.5 * (m0-m1)* (abs(x+1) -abs(x-1));

        xdot = alpha*(y-x-h);
        ydot = x - y+ z;
        zdot  = -beta*y;

        x += xdot * dt
        y += ydot * dt
        z += zdot * dt
        
        x = x % modulo
        y = y % modulo
        z = z % modulo
        
    
        t += dt
        # print(time.time())
    # print(x)
    return (x + y + z) / 3

arr = []
for _ in range(100_000):
    arr.append(random(sys.float_info.max / 1e10))
    if _ % 500 == 0:
        print(_)

fig, ax = plt.subplots()

ax.hist(arr, bins=100, linewidth=0.05, edgecolor="white")
plt.show()

    # if _ % 100 == 0:
    #     print(_, arr[_])

# with open("test.dat", "wb") as f:
#     bytes_array = struct.pack('%sf' % len(arr), *arr)
#     for i in bytes_array:

#     f.write(struct.pack('%sf' % len(arr), *arr))

