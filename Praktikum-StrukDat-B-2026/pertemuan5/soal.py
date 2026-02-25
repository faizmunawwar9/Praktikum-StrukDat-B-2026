nilai_tugas = [70, 85, 90, 65, 80]
nilai_tugas[nilai_tugas.index(65)] = 75
print(nilai_tugas)
nilai_tugas.append(95)
print(nilai_tugas)
nilai_tugas.sort()
print(nilai_tugas)
print(sum(nilai_tugas))

nilai_tugas.append(100)
print(nilai_tugas)
nilai_tugas.append(100)

for x in nilai_tugas:
    if x == 100:
        print("Nilai Sempurna")
        break
    else:
        print("Tidak ada")
        break

# soal 2

kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]    
for x in kumpulan_nilai :
    if x[1] >= 75:
        print(f"Selamat {x[0]}, Anda Lulus!")
    else:
        print(f"Maaf {x[0]}, Anda Harus Remidi")

# soal 3
sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

kedua_sesi = sesi_pagi.intersection(sesi_siang)
print(kedua_sesi)

pagi = sesi_pagi - sesi_siang
siang = sesi_siang - sesi_pagi
pagisiang = pagi.union(siang)
print(pagisiang)

unik = sesi_pagi.union(sesi_siang)
print(unik)

#soal 4
transaksi = [
 {"produk": "Buku", "harga": 10000, "jumlah": 3},
 {"produk": "Pena", "harga": 5000, "jumlah": 10},
 {"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

# A
transaksi[0]['jumlah'] = 8
print(transaksi)

transaksi.append({'"produk" : "pensil, "harga": 2000, "jumlah": 4'})
transaksi.append({'"produk" : "kamus, "harga": 1000, "jumlah": 3'})

for x in range(len(transaksi)):
    total = transaksi[x]['harga'] * transaksi[x]['jumlah']
    print(f'Produk : {transaksi[x]['produk']} ! total :{total}')

                           

