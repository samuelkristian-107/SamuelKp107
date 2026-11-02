# Exercise 6-6: Memeriksa siapa yang belum mengikuti jajak pendapat.
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
orang = ["jen", "sarah", "mike", "phil", "anna"]
for nama in orang:
    if nama in favorite_languages:
        print(f"Terima kasih, {nama.title()}, sudah mengikuti polling.")
    else:
        print(f"{nama.title()}, silakan ikuti polling bahasa pemrograman.")
