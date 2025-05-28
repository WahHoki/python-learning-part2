# continue

# pass -> berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang :{angka}")

    if angka == 3:
        pass
    
    print("bobo")


# continue
angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang :{angka}")

    if angka == 3:
        print("cihuy")
        continue
    
    print("koki")
