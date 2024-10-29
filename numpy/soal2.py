import numpy as np 

matrix = np.arange(10, 33, 2).reshape(3, 4)
flattened_matrix = matrix.flatten() # Melakukan flatten (mengubah menjadi 1D array)


# Mencari nilai statistik
mean_value = np.mean(flattened_matrix)       # Nilai rata-rata
median_value = np.median(flattened_matrix)   # Nilai median
min_value = np.min(flattened_matrix)         # Nilai minimum
max_value = np.max(flattened_matrix)         # Nilai maksimum
std_dev = np.std(flattened_matrix)           # Standar deviasi
variance = np.var(flattened_matrix)          # Variansi

# Menampilkan hasil statistik
print("Matrix 3x4:\n", matrix)
print("\nFlattened array:\n", flattened_matrix)
print("\nNilai Mean:", mean_value)
print("Nilai Median:", median_value)
print("Nilai Minimum:", min_value)
print("Nilai Maksimum:", max_value)
print("Standar Deviasi:", std_dev)
print("Variansi:", variance)
