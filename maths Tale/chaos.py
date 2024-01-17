"""
from math import floor
p,c=2000,2
for _ in range(10):
    p = floor(6*p - 100*c)
    c = floor(5.9*c)
print(p,c)
"""
from matplotlib import pyplot as plt

a = 0.0016
b = 0.4
r = 8.5 * 10**(-5)
s = 0.15
p0 = 2000
c0 = 200
p,c = p0,c0

for _ in range(100):
    p, c = (1+b)*p - a*p*c, (1-s)*c + r*p*c
    plt.scatter(p,c,c='red',s=10)

plt.axis((0,10**4,0,10**3))
plt.show()