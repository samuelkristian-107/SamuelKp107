# Exercise 5-10: Memeriksa nama pengguna tanpa membedakan kapitalisasi.
current_users = ["Andi", "Budi", "Citra", "Dina", "Eko"]
new_users = ["andi", "Fajar", "Gita", "CITRA", "Hana"]
current_lower = [username.lower() for username in current_users]
for username in new_users:
    if username.lower() in current_lower:
        print(f"{username} sudah digunakan. Silakan pilih nama lain.")
    else:
        print(f"{username} tersedia.")
