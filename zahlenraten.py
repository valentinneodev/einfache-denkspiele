#!/usr/bin/env python3

def zahlinput():
    while True:
        try:
            versuch = int(input("Gib eine Zahl ein: "))
            return versuch
        except ValueError:
            print("Das war keine Zahl")



def spiel(zufalls_zahl):
    # initialisierung von Hilfsvariablen
    runden = 1

    # starten des Spiels mit dem ersten Versuch
    print("Errate die Zahl zwischen 0 und 100!")
    print("Gib deinen Ersten Tipp ab.")
    versuch = zahlinput()

    #start der Schleife zum wiederholten raten.
    while (versuch != zufalls_zahl): 
        if versuch > zufalls_zahl:
            print("die gesuchte zahl ist kleiner als "+str(versuch) + ". ")
        if versuch < zufalls_zahl:
            print("die gesuchte zahl ist größer als "+str(versuch) + ". ")
        versuch = zahlinput()
        runden += 1

    return runden


if __name__ == "__main__":
    try:
        # 1. Zahl ausdenken
        import random
        zufalls_zahl = random.randint(0,100)

        # 2. Zahl herausfinden (mensch)
        runden = spiel(zufalls_zahl)

        # 3. Ergebnis anzeigen 
        print("Du hast es geschaft - Glückwunsch! ")
        print("Du hast " +str(runden) + " Versuche gebraucht. ")

    except KeyboardInterrupt: 
        print("\nSpiel abgebrochen")
        print("Schade")