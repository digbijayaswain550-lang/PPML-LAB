import numpy as np


a = np.array([[10, 20, 30],
              [40, 50, 60]])


print("Array:")
print(a)

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))

print("Sum of each column:", np.sum(a, axis=0))
print("Sum of each row:", np.sum(a, axis=1))

b = np.array([1, 2, 3])

print("\nArray A:")
print(a)

print("Array B:")
print(b)

print("Result after broadcasting:")
print(a + b)
