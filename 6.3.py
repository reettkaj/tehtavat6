def gallonat_litroiksi(gallona):
    return gallona * 3.785

def pääohjelma():
    while True:
        gallona = float(input("Anna bensiinin määrä nestegallonoina (syötä negatiivinen lopettaaksesi): "))

        if gallona < 0:
            print("Ohjelma lopetettu.")
            break

        litrat = gallonat_litroiksi(gallona)

        print(f"{gallona} gallonaa on {litrat:.2f} litraa.")

pääohjelma()