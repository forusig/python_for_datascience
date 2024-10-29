# Buatlah Function as an Argument dengan argument sebanyak 2 dan 3. salah satu argument bernilai default.
def operasi(func, a, b, c=4):  # 'c' mempunyai nilai default 4
    return func(a + b + c)

def pangkat(x):
    return x ** 2

hasil_3 = operasi(pangkat, 3, 4)  
print("Hasil operasi pangkat :", hasil_3)
