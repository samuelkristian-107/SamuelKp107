# Exercise 4-15: Contoh program ringkas untuk ditinjau.
# Nama variabel jelas, indentasi konsisten, dan ada spasi di sekitar operator.
def hitung_rata_rata(daftar_nilai):
    total_nilai = sum(daftar_nilai)
    jumlah_nilai = len(daftar_nilai)
    return total_nilai / jumlah_nilai

nilai = [80, 90, 85]
print("Rata-rata:", hitung_rata_rata(nilai))
