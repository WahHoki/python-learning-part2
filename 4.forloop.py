# perulangan (loop)

angka2 = [0,1,2,3,4]
print(angka2)

for i in angka2:
    print(f"i sekarang -> {i}")

print("--------------------------------")

# ini dengan range
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang -> {i}")
print("--------------------------------")

angka2_range = range(1,10)

for i in angka2_range:
    print(f"i sekarang -> {i}")
print("--------------------------------")

data_str = "kamu blok"

for huruf in data_str:
    print(huruf)
