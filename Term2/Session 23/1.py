import numpy as np


arr = np.arange(15).reshape(3, 5)

print(arr)

print(arr.shape)
print(f"Dimentions: {arr.ndim}")
print(f"Data types inside: {arr.dtype.name}")
print(f"Size of arr array: {arr.size}")