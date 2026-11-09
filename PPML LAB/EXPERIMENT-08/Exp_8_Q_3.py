import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:")
print(a)

print("Number of dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)
print("Data type:", a.dtype)
print("Item size:", a.itemsize)

print("Sum:", np.sum(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Mean:", np.mean(a))
print("Standard deviation:", np.std(a))
print("Transpose:")
print(np.transpose(a))
