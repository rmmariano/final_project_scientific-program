
# Exerc. 01) a)

import matplotlib.pyplot as plt
import numpy as np

SIZE_X = 1200
SIZE_Y = 100

#x = np.random.rand(SIZE_X) 
#x = x - 0.5 

x = np.arange(SIZE_X)

y = []

copy_x = list(x)

while len(y) < SIZE_Y:

	i = 0
	sum_values = 0

	while i < 12:
		sum_values = sum_values + value copy_x.pop(0)
		i = i + 1

	y.append(sum_values)


print("\n\nx: ")
print(x)
print("\n\ny: ")
print(y)


#plt.hist(y)
#plt.show()
