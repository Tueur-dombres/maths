import cmath
import matplotlib.pyplot as plt
size = 25
couleurs = ['red', 'blue', 'green', 'black']
"""
r = float(input("Partie réelle : "))
im = float(input("Partie imaginaire : "))
z = complex(r,im)"""
z = complex(2,1.17)
u = z
for k in range(1000):#200
    #print(u.real, u.imag)
    if k%40:plt.scatter(cmath.e**u.real, cmath.e**u.imag, c = couleurs[k%4], s = 2)
    u = z**u
plt.axis((0,size,0,size))
plt.show()
