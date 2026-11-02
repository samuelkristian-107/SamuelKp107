# Exercise 8-5: Fungsi deskripsi kota dengan negara default.
def describe_city(city, country="Indonesia"):
    print(f"{city.title()} berada di {country.title()}.")

describe_city("surakarta")
describe_city("jakarta")
describe_city("tokyo", "jepang")
