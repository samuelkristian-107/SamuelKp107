# Exercise 5-9: Memeriksa apakah daftar pengguna kosong.
users = []
if users:
    for username in users:
        print(f"Halo {username.title()}, selamat datang kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")
