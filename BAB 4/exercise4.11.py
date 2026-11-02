# Exercise 4-11: Menyalin list pizza dan mengubah list salinan.
pizzas = ["margherita", "pepperoni", "vegetarian"]
friend_pizzas = pizzas[:]
pizzas.append("BBQ")
friend_pizzas.append("keju")
print("Pizza saya:")
for pizza in pizzas:
    print(pizza)
print("Pizza teman saya:")
for pizza in friend_pizzas:
    print(pizza)
