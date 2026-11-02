# Exercise 6-1: Menyimpan informasi seseorang dalam dictionary.
person = {
    "first_name": "Budi",
    "last_name": "Santoso",
    "age": 17,
    "city": "Surakarta",
}
for key, value in person.items():
    print(f"{key}: {value}")
