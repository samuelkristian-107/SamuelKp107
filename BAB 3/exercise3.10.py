# Exercise 3-10: Contoh berbagai operasi list.
buah = ["apel", "jeruk", "mangga"]
print("List awal:", buah)
print("Elemen pertama:", buah[0])
buah[1] = "pisang"
buah.append("anggur")
buah.insert(1, "melon")
print("Setelah ditambah/diubah:", buah)
del buah[0]
buah.remove("mangga")
terhapus = buah.pop()
print("Elemen pop:", terhapus)
print("List akhir:", buah)
print("Jumlah elemen:", len(buah))
print("Urutan alfabet:", sorted(buah))
buah.sort(reverse=True)
print("Sort permanen terbalik:", buah)
buah.reverse()
print("Reverse:", buah)
