Z9

9.1
#Plot functions sin(x), cos(x), and exp(-x) in a range [0,10] in the same figure.
#Colors are red, green, and blue, respectively. Lines are solid, dashed, and dotted,
#respectively. Add a legend.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)
f1 = np.sin(x)
f2 = np.cos(x)
f3 = np.exp(-x)
plt.plot(x, f1, "r-", label="sin(x)")
plt.plot(x, f2, "g-", label="cos(x)")
plt.plot(x, f3, "b-", label="exp(-x)")
plt.title("Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

9.2
#Generate n=100 random points in a unit square [0,1]x[0,1]. 
#Points are green if the distance from (0,0) is less then 1; 
#they are red otherwise. The marker area of a point (x,y) should be proportional to |x|+|y|. 

import numpy as np
import matplotlib.pyplot as plt

n = 100
points = np.random.rand(n, 2)
x = points[:,0]
y = points[:,1]

colors = np.where(x**2 + y**2 < 1, "g", "r")

area = 50*(x + y)

plt.scatter(x, y, s=area, c=colors)
plt.title("Randomly generated points in unit sqaure \n Points are green if the distance os less than 1. Otherwise they are red.")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
