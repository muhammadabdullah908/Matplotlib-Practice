import matplotlib.pyplot as plt
import numpy as np

l = np.random.normal(170,10,250)

plt.hist(l, color = 'green')
plt.show()