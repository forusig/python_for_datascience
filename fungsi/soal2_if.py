#conditional if

def cek_no(angka):
    if angka > 0:
        return f"{angka} adalah bilangan positif."
    elif angka < 0:
        return f"{angka} adalah bilangan negatif."
    else:
        return "Ini adalah nol."
        
# Contoh penggunaan
print(cek_no(5))   # Output: 5 adalah bilangan positif.
print(cek_no(-3))  # Output: -3 adalah bilangan negatif.
print(cek_no(0))   # Output: Ini adalah nol.
