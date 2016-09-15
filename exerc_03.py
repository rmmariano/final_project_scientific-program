
# Exerc. 03)


import matplotlib.pyplot as plt
import numpy as np


SIZE_X = 111
SIZE_Z = 100

x = np.random.rand(SIZE_X)
x = x - 0.5

#x = np.arange(SIZE_X)
z = np.array([])

copy_x = list(x)

i = 0
i_s = 0

while len(z) < SIZE_Z:
    somatorio = 0

    for v in range(12):
        somatorio = somatorio + copy_x[i_s]
        i_s = i_s + 1

    i = i + 1

    i_s = i

    z = np.append(z, somatorio)


print("\nvalues of x: ")
print(x)
print("\nvalues of z: ")
print(z)

plt.hist(z)

plt.show()




