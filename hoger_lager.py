from random import randint

getal = randint(0, 100) # random integer = willekeurig geheel getal

while True:
    nummer = int(input("Kies een nummer tussen 0 en 100: "))
    if nummer < getal:
        print("Hoger!")
    if nummer > getal:
        print("Lager!")
    if nummer == getal:
        print("Goed zo!")
        break
