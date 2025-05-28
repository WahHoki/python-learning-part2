# break 
data_int = int(input("hitung sampai 10 ="))

angka = 0

while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_int:
        print("nice")
        break # angka berhenti di 3 dikarenakan penggunaan break

    print("wassap")
