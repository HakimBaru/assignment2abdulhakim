#Inisialisasi sebuah list untuk menyimpan nilai-nilai
grades = []

#Loop tak terbatas untuk memasukkan nilai,-1 untuk break
while True:
    grade = int(input("Masukkan nilai (Ketik -1 untuk mengakhiri): "))
    if grade == -1:
        break  #Break jika -1 untuk keluar dari loop
    grades.append(grade)  # Menambahkan nilai ke dalam list

#Menghitung rata-rata dari nilai-nilai yang dimasukkan
ratarata = sum(grades) // len(grades)

#Output rata-rata
print("Rata-rata nilai:", ratarata)

#Output nilai-nilai dalam urutan yang sama seperti yang dimasukkan
for grade in grades:
    print(grade)