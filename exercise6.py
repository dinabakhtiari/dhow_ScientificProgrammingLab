import numpy as np
def euclidean_norm_manual(x):

    return np.sqrt(np.sum(np.square(x)))

arr = np.array([0.5, -1.2, 3.3, 4.5]) 
print(euclidean_norm_manual(arr))

