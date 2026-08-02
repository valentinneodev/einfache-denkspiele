import random
import time
from turtle import *

t = Turtle()
s = Screen()
s.bgcolor("black")
t.speed(0)
t.hideturtle()

farben_auswahl = ["teal", "blue", "green", "yellow"]
schwierigkeit = 4
gegeben = []
geraten = []

print("Merk dir die Reheinfolge der Farben! ")
time.sleep(3)
print(" \033c ")

def zufall():
    for i in range(schwierigkeit):
        index = random.randint(0,len(farben_auswahl)-1)
        gegeben.append(farben_auswahl[index])

def anzeigen():
    for farbe in gegeben:
        t.color(farbe)
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        print(farbe)
        time.sleep(2)

        t.color("black")
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        print("\033c")
        time.sleep(0.1)

def eingabe():
    global geratene_farbe
    geratene_farbe = input()
    if geratene_farbe not in farben_auswahl:
        return False
    return True

def check():
    for i in range(schwierigkeit):
        if gegeben[i] !=geraten [i]:
            return False

while True:
    zufall()
    anzeigen()

    print("Bitte die Farben nacheinander eingeben: ")
    for i in range(schwierigkeit):
        while not eingabe():
            print("Diese Farbe ist nicht im Spiel ")
        geraten.append(geratene_farbe)

    if check() == False:
        print("Leider Falsch")
        break
    else:
        print("Richtig!\nSchwierigkeit wird erhöht... ")
        schwierigkeit += 1
        gegeben = []
        geraten = []
        time.sleep(2)
        print("\033c")