mahasiswa = {
    "A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
    "A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
    "A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}

print("Mahasiswa dengan IPK di atas 3.5:")
for data in mahasiswa.values():
    if data["ipk"] > 3.5:
        print(data["nama"])

total_ipk = 0
for data in mahasiswa.values():
    total_ipk += data["ipk"]

rata_rata = total_ipk / len(mahasiswa)
print("Rata-rata IPK:", rata_rata)

mahasiswa["A004"] = {
    "nama": "Rina",
    "prodi": "Informatika",
    "ipk": 3.60
}

print("Data mahasiswa setelah ditambah:")
print(mahasiswa)
