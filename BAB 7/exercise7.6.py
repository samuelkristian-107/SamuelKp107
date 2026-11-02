# Exercise 7-6: Tiga pendekatan menghentikan while loop.
print("Versi 1: kondisi pada while (ketik quit untuk selesai).")
pesan = ""
while pesan != "quit":
    pesan = input("Pesan: ").strip().lower()
    if pesan != "quit":
        print("Anda menulis:", pesan)

print("\nVersi 2: variabel aktif.")
aktif = True
while aktif:
    jawaban = input("Lanjut? (ya/tidak): ").strip().lower()
    if jawaban == "tidak":
        aktif = False
    else:
        print("Program masih berjalan.")

print("\nVersi 3: break.")
while True:
    jawaban = input("Ketik quit untuk keluar: ").strip().lower()
    if jawaban == "quit":
        break
    print("Belum keluar.")
