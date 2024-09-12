import random

def heitä_noppa(tahkojen_määrä):
    return random.randint(1, tahkojen_määrä)

def pääohjelma():
    tahkojen_määrä = int(input("Anna nopan tahkojen määrä: "))

    silmäluku = 0
    while silmäluku != tahkojen_määrä:
        silmäluku = heitä_noppa(tahkojen_määrä)
        print(f"Heitetty silmäluku: {silmäluku}")

pääohjelma()