import random

nombres = ["Jimena", "Gaby", "Emilio", "Mariana", "Luis David"]

for nombre in nombres:
    edad = random.randint(10, 75)
    print(f"{nombre} tiene {edad} años.")
