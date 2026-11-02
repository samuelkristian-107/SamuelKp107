# Exercise 3-5: Mengganti tamu yang berhalangan hadir.
tamu = ["B.J. Habibie", "Ki Hajar Dewantara", "R.A. Kartini"]
print(f"{tamu[1]} tidak dapat hadir.")
tamu[1] = "Soekarno"
for nama in tamu:
    print(f"Undangan makan malam untuk {nama}.")
