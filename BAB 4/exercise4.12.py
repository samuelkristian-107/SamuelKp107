# Exercise 4-12: Memastikan kedua list makanan ditampilkan dengan loop.
my_foods = ["nasi goreng", "sate", "bakso"]
friend_foods = my_foods[:]
friend_foods.append("gado-gado")
print("Makanan saya:")
for food in my_foods:
    print(food)
print("Makanan teman:")
for food in friend_foods:
    print(food)
