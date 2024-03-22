from datetime import datetime, timedelta

def main():
    #Tanggal awal adalah tanggal sekarang
    tanggal_mulai = datetime.now()

    try:
        #Input jumlah hari dari pengguna
        hari = int(input("Masukkan jumlah hari: "))

        #Menghitung tanggal akhir dengan menambahkan jumlah hari ke tanggal awal
        tanggal_akhir = tanggal_mulai + timedelta(days=hari)

        #Output tanggal akhir dalam format yang diminta
        print("Tanggal setelah", hari, "hari dari", tanggal_mulai.strftime("%A, %B %d, %Y"), "adalah", tanggal_akhir.strftime("%A, %B %d, %Y"))

    except ValueError:
        print("Masukkan bilangan bulat.")

if __name__ == "__main__":
    main()