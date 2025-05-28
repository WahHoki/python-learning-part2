# list

# kumpulan data numbers
data_angka = [1,2,3]
print(data_angka)

# kumpulan data string
data_string = ["ucup","otong","odah"]
print(data_string)

# kumpulan data bolean
data_boolean = [True, False, True, False]
print(data_boolean)

# data campuran
data_campuran = [1, "adam", 2, "cireng", True, "otong", False]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)
