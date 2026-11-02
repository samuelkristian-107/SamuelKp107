# Exercise 5-8: Sapaan khusus untuk admin.
users = ["admin", "andi", "budi", "citra", "dina"]
for username in users:
    if username == "admin":
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {username.title()}, terima kasih sudah masuk kembali.")
