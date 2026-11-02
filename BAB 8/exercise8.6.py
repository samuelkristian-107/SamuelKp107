# Exercise 8-6: Mengembalikan nama kota dan negara.
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("surakarta", "indonesia"))
print(city_country("tokyo", "jepang"))
print(city_country("paris", "prancis"))
