import numpy as np
correct_elevation = np.array([300, 600, 800, 1000, 1100])
mean_elevation = np.mean(correct_elevation) # 900
print("mean elevation:", mean_elevation)
std_elevation = np.std(correct_elevation)
print("standard deviation of elevation:", std_elevation)
normalization = (correct_elevation - mean_elevation) / std_elevation
print("normalized elevations:", normalization)
print("mean of normalized elevations:", np.mean(normalization))
print("standard deviation of normalized elevations:", np.std(normalization))
