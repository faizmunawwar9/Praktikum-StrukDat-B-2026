kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

keduanya = kelas_A.copy()
keduanya.intersection_update(kelas_B)
print(keduanya)

hanya_A = kelas_A.copy()
hanya_A.difference_update(kelas_B)
print(hanya_A)

gabungan = kelas_A.copy()
gabungan.symmetric_difference_update(kelas_B)
print(gabungan)
