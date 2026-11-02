# Exercise 6-9: Menyimpan satu hingga tiga tempat favorit setiap orang.
favorite_places = {
    "Andi": ["Bali", "Yogyakarta"],
    "Budi": ["Bandung"],
    "Citra": ["Tokyo", "Seoul", "Paris"],
}
for nama, tempat in favorite_places.items():
    print(f"Tempat favorit {nama}:")
    for lokasi in tempat:
        print(f"- {lokasi}")
