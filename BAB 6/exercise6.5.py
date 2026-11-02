# Exercise 6-5: Menyimpan sungai dan negara yang dilaluinya.
rivers = {
    "Nil": "Mesir",
    "Amazon": "Brasil",
    "Kapuas": "Indonesia",
}
for sungai, negara in rivers.items():
    print(f"Sungai {sungai} mengalir melalui {negara}.")
print("Nama sungai:", list(rivers.keys()))
print("Negara:", list(rivers.values()))
