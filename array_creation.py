import numpy as np
my_array = np.array([10, 9, 8])
#print(my_array)

my_2d_array = np.array([[1, 3, 5, 7],[2, 4, 6, 8]], dtype=np.float32)
print(my_2d_array[1, 1])
print("-------------")
print(my_2d_array[1])
print("-------------")
print(my_2d_array[:, 2])
print("-------------")
print(my_array.shape)
print(my_2d_array.shape)
print("-------------")
print(my_2d_array.dtype)
print("-------------")

