# Exercise 7-10: Polling tujuan liburan impian.
polling = {}
aktif = True
while aktif:
    nama = input("Nama Anda: ").strip()
    tujuan = input("Tujuan liburan impian: ").strip()
    if nama and tujuan:
        polling[nama] = tujuan
    lagi = input("Apakah ada peserta lain? (ya/tidak): ").strip().lower()
    if lagi != "ya":
        aktif = False
print("\nHasil polling:")
for nama, tujuan in polling.items():
    print(f"{nama} ingin berlibur ke {tujuan}.")
