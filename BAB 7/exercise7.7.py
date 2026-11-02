# Exercise 7-7: Contoh loop berulang dengan penghentian yang aman.
# Loop ini dapat dihentikan dengan mengetik 'stop', sehingga tidak mengunci VS Code.
while True:
    perintah = input("Program berjalan. Ketik stop untuk mengakhiri: ").strip().lower()
    if perintah == "stop":
        print("Loop dihentikan.")
        break
    print("Loop masih berjalan.")
