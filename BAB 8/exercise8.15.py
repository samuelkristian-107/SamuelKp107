# Exercise 8-15: Memisahkan fungsi ke dalam modul dan menggunakannya.
# Simulasi dua fungsi yang biasanya disimpan dalam file printing_functions.py.
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        design = unprinted_designs.pop()
        print(f"Mencetak model: {design}")
        completed_models.append(design)

def show_completed_models(completed_models):
    print("\nModel yang sudah dicetak:")
    for model in completed_models:
        print(model)

unprinted = ["robot", "gantungan kunci", "miniatur mobil"]
completed = []
print_models(unprinted[:], completed)
show_completed_models(completed)
