try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil = angka1 / angka2
except ValueError:
    print("Input harus angka.")
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol.")
else:
    print("Hasil pembagian adalah:", hasil)
finally:
    print("Selesai")
