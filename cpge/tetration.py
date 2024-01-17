import cmath
import matplotlib.pyplot as plt
couleurs = ['red', 'blue', 'green']
i = complex(-.2,-1)
z = 1
l = complex(0.4382829367422192, 0.3605924719347524)
for k in range(200):#200
    z = i**z
    #a = z
    a=z
    #print(z.real, z.imag)
    plt.scatter(a.real, a.imag, c = couleurs[0], s = 2)
    #plt.scatter(k, abs(a), c = couleurs[k%3], s = 4)
#plt.axis((0,1,0,1))
plt.axis((-2,2,-2,2))
plt.show()