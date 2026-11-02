# Exercise 6-7: Menyimpan beberapa dictionary orang dalam sebuah list.
people = [
    {"first_name": "Budi", "last_name": "Santoso", "age": 17, "city": "Surakarta"},
    {"first_name": "Citra", "last_name": "Lestari", "age": 18, "city": "Semarang"},
    {"first_name": "Dina", "last_name": "Putri", "age": 17, "city": "Yogyakarta"},
]
for person in people:
    print("\nData orang:")
    for key, value in person.items():
        print(f"{key}: {value}")
