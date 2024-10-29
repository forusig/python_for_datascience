# Create
tuple_kata = ('Kamu', 'Apel', 'Merdeka')

# Update (membuat tuple baru)
tuple_kata = ('Pisang',) + tuple_kata[1:]  # Mengubah 'Kamu' menjadi 'Pisang'

# Delete (membuat tuple baru)
tuple_kata = tuple_kata[1:]  # Menghapus elemen pertama

# For Loop
for kata in tuple_kata:
    print(kata)
