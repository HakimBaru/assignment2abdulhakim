class BMI_Calculator:
    def __init__(self, berat, tinggi):
        self.set_berat(berat)  #Berat dalam kilogram
        self.set_tinggi(tinggi)  #Tinggi dalam meter

    def set_berat(self, berat):
        if berat <= 0:
            raise ValueError("Masukkan berat dalam angka positif.")
        self._berat = berat

    def get_berat(self):
        return self._berat

    def set_tinggi(self, tinggi):
        if tinggi <= 0:
            raise ValueError("Masukkan tinggi dalam angka positif.")
        self._tinggi = tinggi

    def get_tinggi(self):
        return self._tinggi

    def BMI_Value(self):
        return self.get_berat() / (self.get_tinggi() ** 2)


if __name__ == "__main__":
    #Input berat dalam kilogram dan tinggi dalam sentimeter
    berat = float(input("Masukkan berat dalam kg (contoh: 88): "))
    tinggi = float(input("Masukkan tinggi dalam m (contoh: 1.80): "))

    #Membuat objek BMI_Calculator dengan nilai berat dan tinggi yang dimasukkan
    person = BMI_Calculator(berat, tinggi)

    #Menghitung nilai BMI menggunakan metode BMI_Value dari objek person
    bmi = person.BMI_Value()

    #Output nilai BMI
    print("BMI:", bmi)
