# Exercise 7-9: Menghapus semua pesanan pastrami.
sandwich_orders = ["tuna", "pastrami", "ayam", "pastrami", "telur", "pastrami"]
print("Pastrami sedang tidak tersedia.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
finished_sandwiches = []
while sandwich_orders:
    pesanan = sandwich_orders.pop(0)
    print(f"Sandwich {pesanan} sedang dibuat.")
    finished_sandwiches.append(pesanan)
print("Pesanan selesai:", finished_sandwiches)
