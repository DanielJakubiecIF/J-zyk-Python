Z14

#Approximate the value of pi using a Monte Carlo method.
#Try different numbers of input points (10, 10^2, 10^3, 10^4, 10^5, 10^6).
#Try to get faster code with Numba (remember that the first run is slower). 

from numba import jit
import random


@jit(nopython=True)
def pi(n=1000):

    area = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            area += 1
    return (4.0 * area) / n

N = pow(10,8)
print("n = {}, pi = {}".format(N, pi(N)))
