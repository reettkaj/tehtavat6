def poista_parittomat(lista):
    parilliset = [luku for luku in lista if luku % 2 == 0]
    return parilliset

def pääohjelma():
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    karsittu_lista = poista_parittomat(luvut)

    print(f"Alkuperäinen lista: {luvut}")
    print(f"Karsittu lista (vain parilliset luvut): {karsittu_lista}")

pääohjelma()