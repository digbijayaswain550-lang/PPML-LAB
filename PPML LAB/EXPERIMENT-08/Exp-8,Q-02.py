import numpy as np
a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1.5, 2.5, 3.5], dtype=np.float64)
c = np.array([True, False, True], dtype=np.bool_)

print("Integer:", a, a.dtype)
print("Float:", b, b.dtype)
print("Boolean:", c, c.dtype)

arr1 = np.array([1, 2, 3])                 
arr2 = np.array([[1, 2], [3, 4]])         
arr3 = np.array([[[1, 2], [3, 4]]])       

print("1-D Array:\n", arr1)
print("2-D Array:\n", arr2)
print("3-D Array:\n", arr3)
