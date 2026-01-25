import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
pixel_x = 30
pixel_y= 40
 
scatter = plt.scatter(X[:,pixel_x], X[:, pixel_y], c=y, cmap="viridis")
plt.colorbar(scatter)
plt.xlabel("pixel 30")
plt.ylabel("pixel 40")
plt.show()
