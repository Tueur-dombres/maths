import cmath
import matplotlib.pyplot as plt
couleurs = ['red', 'blue', 'green']
i = complex(0,1)
z = 1
l = complex(0.4382829367422192, 0.3605924719347524)
for k in range(30):#200
    z = i**z
    #a = z
    a=z-l
    print(z.real, z.imag)
    #plt.scatter(a.real, a.imag, c = couleurs[k%3], s = 2)
    plt.scatter(k, abs(a), c = couleurs[k%3], s = 2)
#plt.axis((0,1,0,1))
plt.axis((0,30,0,.8))
plt.show()