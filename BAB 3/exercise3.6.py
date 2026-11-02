# Exercise 3-6: Menambah tamu dan menyisipkan tamu baru.
tamu = ["B.J. Habibie", "Soekarno", "R.A. Kartini"]
print("Saya menemukan meja makan yang lebih besar.")
tamu.insert(0, "Mohammad Hatta")
tamu.insert(len(tamu) // 2, "Dewi Sartika")
tamu.append("Ki Hajar Dewantara")
for nama in tamu:
    print(f"Undangan makan malam untuk {nama}.")
