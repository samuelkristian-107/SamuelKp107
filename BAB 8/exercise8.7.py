# Exercise 8-7: Fungsi yang membangun dictionary album.
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album

print(make_album("Tulus", "Manusia"))
print(make_album("Sheila On 7", "07 Des"))
print(make_album("Dewa 19", "Bintang Lima", 11))
