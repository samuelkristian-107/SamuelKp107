# Exercise 6-11: Dictionary kota dengan informasi bertingkat.
cities = {
    "Surakarta": {"country": "Indonesia", "population": 522000, "fact": "Dikenal dengan budaya Jawa."},
    "Tokyo": {"country": "Jepang", "population": 14000000, "fact": "Merupakan ibu kota Jepang."},
    "Paris": {"country": "Prancis", "population": 2100000, "fact": "Dikenal dengan Menara Eiffel."},
}
for kota, info in cities.items():
    print(f"\n{kota}:")
    print(f"Negara: {info['country']}")
    print(f"Perkiraan populasi: {info['population']:,}")
    print(f"Fakta: {info['fact']}")
