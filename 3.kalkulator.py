# Latihan membuat kalkulator sederhana
angka1 = float(input("Masukan angka pertama :"))
operator = input("masukan operator(+,-,*,/) :")
angka2 = float(input("Masukan angka kedua :"))

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil : {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil : {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil : {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasil : {hasil}")
else:
    print("pencarian kamu salah")
