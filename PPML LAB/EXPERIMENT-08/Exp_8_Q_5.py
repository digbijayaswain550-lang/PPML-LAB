import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Original Array:")
print(arr)

np.save("my_array.npy", arr)

print("\nArray saved successfully.")

loaded_arr = np.load("my_array.npy")

print("\nLoaded Array:")
print(loaded_arr)
