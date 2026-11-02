# Exercise 6-3: Membuat glosarium istilah Python.
glossary = {
    "variabel": "Nama untuk menyimpan atau merujuk suatu nilai.",
    "list": "Struktur data untuk menyimpan beberapa nilai berurutan.",
    "tuple": "Kumpulan data berurutan yang tidak dapat diubah.",
    "dictionary": "Struktur data pasangan kunci dan nilai.",
    "loop": "Perintah untuk mengulang blok kode.",
}
for istilah, arti in glossary.items():
    print(f"{istilah.title()}: {arti}\n")
