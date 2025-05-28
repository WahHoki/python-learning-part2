# latihan perulangan segitiga

sisi = 6

# dummy variable
print ("awal dari for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

count = 6
for i in range(sisi):
    print("*"*count)
    count -= 1

print("akhir dari for")


# menggunakan while
print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir dari while")


# hanya ganjil saja 

print("awal while")
count = 1
while True:
    # akan kembali keatas jika ganjil
    if count%2:
        print("*"*count)
        count += 1
    else:
    # akan print jika genap
        count += 1
        continue

    # akan break jika melebihi sisi
    if count > sisi:
        break

print("akhir dari while")


# hanya ganjil saja 

print("awal while")
count = 1
spasi = int(sisi/2)
while True:
    # akan kembali keatas jika ganjil
    if count%2:
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
    # akan print jika genap
        count += 1
        continue

    # akan break jika melebihi sisi
    if count > sisi:
        break

print("akhir dari while")

