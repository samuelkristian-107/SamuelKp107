# Exercise 6-10: Mengembangkan angka favorit menjadi beberapa angka per orang.
favorite_numbers = {
    "Andi": [7, 9],
    "Budi": [10, 2],
    "Citra": [3, 8],
    "Dina": [5],
    "Eko": [12, 4, 6],
}
for nama, angka_list in favorite_numbers.items():
    print(f"Angka favorit {nama}: {', '.join(map(str, angka_list))}")
