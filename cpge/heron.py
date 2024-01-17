from math import log10 as log
u = 2
p = 49

for i in range(3):
    u = u/2 + 1/u*p/2

print(u, p**0.5, log(u - p**0.5))