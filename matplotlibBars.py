import matplotlib.pyplot as plt
import numpy as np

# First graph - vertical bars
x = np.array(['A','B','C','D','E'])
y = np.array([3,5,7,9,11])
plt.bar(x,y, color= 'red', width=0.8)
plt.show()

# Second graph - horizontal bars  
z = np.array(['L','M','N','O'])
t = np.array([5,10,15,20])  # Fixed: added brackets
plt.barh(z,t, color= 'green', height=0.8)
plt.show()