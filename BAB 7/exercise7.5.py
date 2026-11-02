# Exercise 7-5: Menghitung harga tiket menurut usia.
while True:
    jawaban = input("Masukkan usia (atau 'quit' untuk selesai): ").strip()
    if jawaban.lower() == "quit":
        break
    if not jawaban.isdigit():
        print("Masukkan usia berupa angka.")
        continue
    usia = int(jawaban)
    if usia < 3:
        harga = 0
    elif usia <= 12:
        harga = 10
    else:
        harga = 15
    print(f"Harga tiket: ${harga}")
