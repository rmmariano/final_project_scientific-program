
# Exerc. 02)


import matplotlib.pyplot as plt
import numpy as np


SIZE_X = 1200
SIZE_Y = 100


x = np.random.rand(SIZE_X)
x = x - 0.5

#x.clip(-6,6)

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



print("\nvalues of x: ")
print(x)
print("\nvalues of y: ")
print(y)

plt.hist(y)

plt.show()
