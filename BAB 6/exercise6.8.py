# Exercise 6-8: Menyimpan data beberapa hewan peliharaan.
pets = [
    {"animal": "kucing", "owner": "Andi"},
    {"animal": "anjing", "owner": "Budi"},
    {"animal": "kelinci", "owner": "Citra"},
]
for pet in pets:
    print(f"Hewan: {pet['animal']}; pemilik: {pet['owner']}.")
