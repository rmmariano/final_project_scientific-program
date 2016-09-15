
# Exerc. 01) a)

import matplotlib.pyplot as plt
import numpy as np

# create 100 values between 0 and 1
x = np.random.rand(100)
# do the values between -0.5 and 0.5
x = x - 0.5

print("values of x: ")
print(x)

plt.hist(x)

#a.clip(0,5)

plt.show()
