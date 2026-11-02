# Exercise 8-16: Contoh empat gaya import fungsi.
# Modul standar math dipakai sebagai contoh modul yang tersedia di Python.
import math
print("Import modul:", math.sqrt(81))

from math import ceil
print("Import fungsi tertentu:", ceil(4.2))

from math import floor as pembulatan_bawah
print("Import dengan alias:", pembulatan_bawah(4.8))

import math as matematika
print("Import modul dengan alias:", matematika.factorial(5))
