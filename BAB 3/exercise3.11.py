# Exercise 3-11: Memahami IndexError dengan penanganan aman.
kendaraan = ["Honda", "Yamaha", "Suzuki"]
print("List:", kendaraan)
print("Indeks yang benar:", kendaraan[2])
try:
    print(kendaraan[3])  # Indeks ini sengaja di luar jangkauan.
except IndexError:
    print("IndexError tertangkap: indeks 3 tidak tersedia.")
