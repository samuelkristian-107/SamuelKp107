# Exercise 6-4: Menampilkan glosarium dengan perulangan.
glossary = {
    "variabel": "Tempat memberi nama pada suatu nilai.",
    "list": "Kumpulan elemen yang dapat diubah.",
    "tuple": "Kumpulan elemen yang tidak dapat diubah.",
    "dictionary": "Kumpulan pasangan key-value.",
    "loop": "Struktur untuk menjalankan kode berulang.",
    "string": "Tipe data berupa teks.",
    "integer": "Tipe data bilangan bulat.",
}
for istilah, arti in glossary.items():
    print(f"{istilah.title()} berarti {arti}")
