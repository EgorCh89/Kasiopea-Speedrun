#!/usr/bin/env python3
import sys, pprint

def ponozky(data):
    """Upravte tuto funkci"""
    pary = dict()
    vzdalenost = 0

    for i in range(0,len(data)):
        if pary.get(int(data[i])) is None:
            pary[int(data[i])] = [i]
        else:
            pary[int(data[i])].append(i)

    posledni = 0
    for i in pary.keys():

        vzdalenost += abs(posledni - pary.get(i)[0])

        vzdalenost += pary[i][1] - pary.get(i)[0]

        posledni = pary[i][1]


        
    return vzdalenost

    



# Načítání vstupu


def precti_vstup(input, output):
    pocet_problemu = int(input.readline())
    wad
    

    for _ in range(pocet_problemu):
        pocet = int(input.readline())
        data = str(input.readline()).split(" ")

        reseni = ponozky(data)
        output.write(f"{reseni}\n")

NAZVY_SOUBORU = [
    ("E-lehky.txt", "E-lehky-vystup.txt"),
    ("E-tezky.txt", "E-tezky-vystup.txt"),
]

soubor_nalezen = False

for nazev_vstupu, nazev_vystupu in NAZVY_SOUBORU:
    try:
        with open(nazev_vstupu, "r", 1, "utf-8") as vstup:
            with open(nazev_vystupu, "w", 1, "utf-8") as vystup:
                precti_vstup(vstup, vystup)

        soubor_nalezen = True

    except FileNotFoundError:
        pass

if not soubor_nalezen:
    precti_vstup(sys.stdin, sys.stdout)