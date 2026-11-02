# Exercise 8-17: Contoh fungsi dengan penamaan dan dokumentasi yang jelas.
def hitung_luas_persegi_panjang(panjang, lebar):
    """Mengembalikan luas persegi panjang."""
    return panjang * lebar


def tampilkan_hasil(luas):
    """Menampilkan luas yang telah dihitung."""
    print(f"Luas persegi panjang: {luas}")


hasil = hitung_luas_persegi_panjang(8, 5)
tampilkan_hasil(hasil)
