# Exercise 8-8: Mengumpulkan album melalui input berulang.
def make_album(artist, title):
    return {"artist": artist, "title": title}

while True:
    print("\nMasukkan data album (ketik q untuk berhenti).")
    artist = input("Nama artis: ").strip()
    if artist.lower() == "q":
        break
    title = input("Judul album: ").strip()
    if title.lower() == "q":
        break
    print(make_album(artist, title))
