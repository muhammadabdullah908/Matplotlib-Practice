import matplotlib.pyplot as plt
import numpy as np

p = np.array([78, 21, 0.93, 0.04 ])

l = ['Nitrogen', 'Oxygen', 'Argon', 'Carbon Dioxide']

t = 'Composition of Air'

e = [0, 0, 0.1, 0]

c = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

plt.pie(p, labels=l, startangle=110, explode=e, shadow=True, colors=c)
plt.title(t)
plt.legend(title = 'Gases')
plt.show()