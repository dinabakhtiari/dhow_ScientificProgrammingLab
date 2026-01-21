import numpy as np
def euclidean_norm_2d(X):

  return np.sqrt(np.sum(np.square(X), axis=1))

my_matrix = np.array([[0.5, -1.2, 4.5],
                      [-3.2, 1.9, 2.7]])
print(euclidean_norm_2d(my_matrix))