def korok():
    print("II/A, B, C:")
    lista = []
    while len(lista) < 5:
        szam = int(input("\tÉletkor megadása [0-120]: "))
        if 0 <= szam <= 120:
            lista.append(szam)
        else:
            print("\tNem jó, próbáld újra!")

    for ix in range(len(lista)-1):
        print(lista[ix], end=":")
    print(lista[len(lista)-1])

    print("II/D, E:")
    konzolra_ir(elso_idos(lista))
    print("II/F:")
    fajl_ir(elso_idos(lista))

def elso_idos(lista):
    for ix in range(len(lista)):
        if lista[ix] > 70:
            return ix
    return "nincs"

def konzolra_ir(eredmeny):
    print("Első idős ember korának helye a listában:", eredmeny)

def fajl_ir(eredmeny):
    open("oreg.txt", "w", encoding="utf-8").write("Első idős ember korának helye a listában:"+ eredmeny)
