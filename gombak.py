from gomba import Gomba


def gombak():
    olvas = open("gombak.txt", "r", encoding="utf-8")
    olvas.readline()
    nyers = olvas.readlines()
    gombak = []

    for ix in nyers:
        gombak.append(Gomba(ix.strip()))
    print("III/A, B:")
    print("\tA gombák száma:", gombak_szama(gombak))

    print("III/C:")
    print("\tAz első papsapkagomba neve:", papsapka(gombak))

    print("III/D:")
    print("A tinóru gombák száma:", tinoru(gombak))


def gombak_szama(lista):
    return len(lista)


def papsapka(lista):
    for ix in lista:
        if "papsapkagombák" in ix.nemzettseg:
            return ix.nev
    return "nincs ilyen"


def tinoru(lista):
    db = 0
    for ix in lista:
        if ix.nemzettseg == "tinóru":
            db += 1
    return db
