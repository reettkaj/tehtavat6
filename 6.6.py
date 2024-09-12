import math

def laske_yksikkohinta(halkaisija, hinta):
    säde = halkaisija / 2
    pinta_ala = math.pi * (säde / 100) ** 2
    return hinta / pinta_ala

def pääohjelma():
    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta (euroa): "))

    halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna toisen pizzan hinta (euroa): "))

    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} euroa/m²")
    print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} euroa/m²")

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat ovat yhtä edullisia.")

pääohjelma()