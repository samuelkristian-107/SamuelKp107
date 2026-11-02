# Exercise 7-8: Memproses pesanan sandwich satu per satu.
sandwich_orders = ["tuna", "ayam", "telur", "daging"]
finished_sandwiches = []
while sandwich_orders:
    pesanan = sandwich_orders.pop(0)
    print(f"Saya membuat sandwich {pesanan}.")
    finished_sandwiches.append(pesanan)
print("\nSandwich selesai dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)
