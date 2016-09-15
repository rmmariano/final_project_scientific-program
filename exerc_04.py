# Exerc. 02)

import matplotlib.pyplot as plt
import numpy as np

SIZE_X = 1200
SIZE_Y = 100

x = np.random.rand(SIZE_X)
x = x - 0.5
#x = np.arange(SIZE_X)
y = np.array([])

copy_x = list(x)

while len(y) < SIZE_Y:
	i = 0
	sum_values = 0

	while i < 12:
		sum_values = sum_values + copy_x.pop(0)
		i = i + 1

	y = np.append(y, sum_values)

'''
print("\nvalues of x: ")
print(x)
print("\nvalues of y: ")
print(y)

plt.hist(y)

plt.show()
'''

# Exerc. 03)

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


'''
print("\nvalues of x: ")
print(x)
print("\nvalues of z: ")
print(z)

plt.hist(z)

plt.show()
'''

# Exerc. 4)

# valor presente (m1)

y_valor_presente = np.array([])

m1[0]=y[0]
m2[0]=y[0]
m3[0]=y[0]

for yi in range(1,3):


yi=2
    m1[yi]=y[yi-1]
    m2[yi]=sum(y[:yi-1])/yi
    m3[yi]=sum(12*y[:yi-1]+11*y[:yi-2])/72

    print(yi)



