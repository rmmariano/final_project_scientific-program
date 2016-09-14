
# Exerc. 01) b)

import matplotlib.pyplot as plt
import numpy as np

# create 200 values between 0 and 1
x = np.random.rand(200) 
# do the values between -0.5 and 0.5
x = x - 0.5 

print("values of x: ")
print(x)

plt.hist(x)

plt.show()
