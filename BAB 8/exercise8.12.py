# Exercise 8-12: Fungsi dengan jumlah argumen topping yang fleksibel.
def make_sandwich(*items):
    print("\nSandwich dengan isi:")
    for item in items:
        print(f"- {item}")

make_sandwich("keju", "selada")
make_sandwich("ayam", "saus", "tomat")
make_sandwich("telur")
