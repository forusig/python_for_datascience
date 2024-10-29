#conditional loop (while)
def sum(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# Contoh penggunaan
print(sum(5))  # Output: 15 (karena 1+2+3+4+5 = 15)
