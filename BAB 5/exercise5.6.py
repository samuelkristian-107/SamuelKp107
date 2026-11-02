# Exercise 5-6: Mengelompokkan tahap kehidupan berdasarkan usia.
usia = 17
if usia < 2:
    tahap = "bayi"
elif usia < 4:
    tahap = "balita"
elif usia < 13:
    tahap = "anak-anak"
elif usia < 20:
    tahap = "remaja"
elif usia < 65:
    tahap = "dewasa"
else:
    tahap = "lanjut usia"
print(f"Usia {usia} tahun termasuk tahap {tahap}.")
