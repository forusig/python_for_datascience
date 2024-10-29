# Create
buah = {'apel': 5, 'pisang': 3}

# Update
buah['apel'] = 7  # Mengubah jumlah apel menjadi 7

# Delete
del buah['pisang']  # Menghapus pisang

# For Loop
for buah, jumlah in buah.items():
    print(f"{buah}: {jumlah}")
