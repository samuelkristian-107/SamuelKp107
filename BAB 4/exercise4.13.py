# Exercise 4-13: Menggunakan tuple menu tetap lalu menggantinya.
menu = ("nasi", "ayam bakar", "sayur", "tempe", "buah")
print("Menu awal:")
for makanan in menu:
    print(makanan)
# Tuple tidak dapat diubah per elemen; buat tuple baru untuk menu revisi.
menu = ("nasi", "ikan", "sayur", "tahu", "sup")
print("Menu baru:")
for makanan in menu:
    print(makanan)
