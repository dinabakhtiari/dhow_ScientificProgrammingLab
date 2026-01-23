import numpy as np
from matplotlib import pyplot as plt
x_values = np.linspace(-10, 10, 1000)
plt.figure()
plt.plot(x_values, np.sin(x_values), label="Sinusoid")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Matplotlib example")
plt.legend(loc="upper left")
plt.show()

