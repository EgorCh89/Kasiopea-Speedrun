#!/usr/bin/env python3
import sys

def rekordy(data):
    """Upravte tuto funkci"""
    max:int = int(data[0])
    pocet:int = 1
    for i in data:
        if int(i) > max:
            max = int(i)
            pocet+=1
    
    return pocet



# Načítání vstupu


def precti_vstup(input, output):
    pocet_problemu = int(input.readline())

    for _ in range(pocet_problemu):
        pocet = int(input.readline())
        data = str(input.readline()).split(" ")

        reseni = rekordy(data)
        output.write(f"{reseni}\n")


NAZVY_SOUBORU = [
    ("B-lehky.txt", "B-lehky-vystup.txt"),
    ("B-tezky.txt", "B-tezky-vystup.txt"),
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