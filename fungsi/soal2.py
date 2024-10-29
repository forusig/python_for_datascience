#args dan kwargs
def sapa(*args, **kwargs):
    sapaan = "Halo, "
    for nama in args:
        sapaan += nama + ", "
    
    sapaan = sapaan.rstrip(", ")  # Menghapus koma terakhir

    if kwargs.get("tanda_baca"):
        sapaan += kwargs["tanda_baca"]
    else:
        sapaan += "!"
    
    return sapaan

# Contoh penggunaan
print(sapa("Andi", "Budi", "Cici"))  # Output: Halo, Andi, Budi, Cici!
print(sapa("Andi", tanda_baca="."))  # Output: Halo, Andi.
