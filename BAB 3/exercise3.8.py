# Exercise 3-8: Mengelola daftar tempat yang ingin dikunjungi.
tempat = ["Tokyo", "Madinah", "Paris", "Bali", "Istanbul"]
print("Daftar asli:", tempat)
print("Urut sementara:", sorted(tempat))
print("Asli tetap:", tempat)
print("Urut terbalik sementara:", sorted(tempat, reverse=True))
tempat.reverse()
print("Setelah reverse:", tempat)
tempat.reverse()
print("Kembali seperti semula:", tempat)
tempat.sort()
print("Urut permanen:", tempat)
tempat.sort(reverse=True)
print("Urut permanen terbalik:", tempat)
