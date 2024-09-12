import random
def heitänoppa():
    return random.randint(1, 6)

def pääohjelma():
    silmäluku = 0
    while silmäluku != 6:
        silmäluku = heitänoppa()
        print(f"Heitetty silmäluku: {silmäluku}")

pääohjelma()