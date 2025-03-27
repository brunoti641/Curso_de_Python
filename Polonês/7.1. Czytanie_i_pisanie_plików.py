# 7.1. Dateien lesen und schreiben
with open("daten.txt", "w") as datei:
    datei.write("Hallo, Datei!")

with open("daten.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)