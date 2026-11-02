# Exercise 7-4: Menerima topping sampai pengguna mengetik quit.
while True:
    topping = input("Masukkan topping (ketik 'quit' untuk selesai): ").strip()
    if topping.lower() == "quit":
        break
    if topping:
        print(f"Menambahkan {topping} ke pizza Anda.")
print("Pesanan pizza selesai.")
