import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0.0001,1,100)
Y = np.sin(1/X)

plt.plot(X,Y)
plt.plot(X,np.sin(X))
plt.title(r'Bustamante')