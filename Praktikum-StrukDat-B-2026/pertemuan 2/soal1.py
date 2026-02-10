angka = [10, 20, 30, 40, 50]

angka.append(60)
print(angka)
angka.remove(20)
print(angka)
angka.sort(reverse = True)
print(angka)
jumlah = 0
rata = 0
for x in angka:
    jumlah = jumlah + x

angka = jumlah
rata = jumlah / 5
print(rata)
