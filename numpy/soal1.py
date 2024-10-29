import numpy as np
array_1d = np.array([1,2,3,4])
array_2d = np.array([[5,6,7], [8,9,10]])
array_3d = np.array([[[11, 12], [13, 14]], [[15, 16], [17, 18]]])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

join = np.concatenate((array_2d, matrix))
joinv = np.vstack((array_2d, matrix))
split = np.split(array_1d, 2) # memisahkan jadi 2 bagian
penjumlahan = matrix + array_2d # operasi penjumlahan matrix
perkalian = matrix*array_2d # operasi perkalian
pangkat = np.power(matrix, 3) # operasi pangkat dengan fungsi power()

# pemanggilan
print("\nArray 1D:\n", array_1d)
print("\nArray 2D:\n", array_2d)
print("\nArray 3D:\n", array_3d)
print("\nJoin:\n", join)
print("\nJoin secara vertikal:\n", joinv)
print("\nSplit:\n", split)
print("\nMatrix penjumlahan:\n", penjumlahan)
print("\nMatrix Perkalian:\n", perkalian)
print("\nMatrix Pangkat:\n", pangkat)
