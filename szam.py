import random


def szam():
    szam = random.randint(1, 50)
    szoveg = ""
    print("I/A:")
    print("\tA generált szám:", szam)
    print("I/B:")
    if szam % 5 == 0 and szam % 3 == 0:
        szoveg = "A szám öttel és hárommal is osztható!"
    elif szam % 5 == 0:
        szoveg = "A szám öttel osztható!"
    elif szam % 3 == 0:
        szoveg = "A szám hárommal osztható!"
    else:
        szoveg = "A szám öttel sem és hárommal sem osztható!"
    print("\t" + szoveg)
