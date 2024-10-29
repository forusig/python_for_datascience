# Create
list_kata = ["Kamu", "Apel", "Merdeka"]

# Menambahkan data baru
list_kata.append("Makan")  # Menambahkan "Makan" ke akhir list

# Update
list_kata[1] = "Pisang"  # Mengubah "Apel" menjadi "Pisang" di indeks ke-1

# Delete
list_kata.remove("Merdeka")  # Menghapus elemen "Merdeka" dari list

# For Loop
for kata in list_kata:
    print(kata)
