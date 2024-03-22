def main():
    total = 0

    #Menginisialisasi variabel untuk menyimpan angka yang dimasukkan
    numbers = []

    #Loop untuk membaca angka dari pengguna
    while True:
        num = float(input("Masukkan angka (atau -1 untuk berhenti): "))
        
        #Keluar dari loop jika -1 dimasukkan
        if num == -1:
            break
        
        #Menambahkan angka ke total
        total += num
        
        #Menambahkan angka ke daftar
        numbers.append(num)

    #Output total dengan format desimal dua digit
    print("Total: {:.2f}".format(total))

    #Output angka-angka yang dimasukkan
    print("Angka yang dimasukkan:")
    for num in numbers:
        print("{:.2f}".format(num))

if __name__ == "__main__":
    main()