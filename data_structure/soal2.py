# Daftar kata
list_kata = ['Kamu', 'Apel', 'Merdeka', 'Lontong', 'Ikan']

# Loop untuk memeriksa setiap kata dan mencetak jika mengandung 'ka'
for kata in list_kata:
    if 'ka' in kata.lower():  # Gunakan lower() agar case-insensitive
        print(kata)
