# Exercise 3-7: Mempertahankan dua tamu setelah daftar dipangkas.
tamu = ["Habibie", "Soekarno", "Kartini", "Hatta", "Dewantara", "Sartika"]
print("Maaf, hanya dua orang yang dapat diundang.")
while len(tamu) > 2:
    dihapus = tamu.pop()
    print(f"Maaf {dihapus}, undangan dibatalkan.")
for nama in tamu:
    print(f"{nama}, undangan Anda tetap berlaku.")
del tamu[:]
print("Daftar tamu akhir:", tamu)
