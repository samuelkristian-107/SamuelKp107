# Exercise 8-14: Membuat dictionary mobil dengan informasi tambahan fleksibel.
def make_car(manufacturer, model, **options):
    car = {"manufacturer": manufacturer, "model": model}
    car.update(options)
    return car

mobil = make_car("subaru", "outback", color="blue", tow_package=True)
print(mobil)
