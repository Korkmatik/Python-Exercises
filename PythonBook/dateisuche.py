from os import walk
from os.path import getmtime, join, normcase
import time

SUCHBERICHT = """
Datei und Zeitpunkt der letzten Änderung:
{}"""

class Dateisuche:
    def __init__(self, verzeichnisbaum, zeitintervall):
        self.ergebnis = []
        self.verzeichnisbaum = verzeichnisbaum
        self.zeitintervall = time.time() - float(zeitintervall) *3600

        self.liste = walk(self.verzeichnisbaum)

        for pfad, unterverzeichnis, dateien in self.liste:
            for datei in dateien:
                dateipfad = normcase(join(pfad, datei))

                if getmtime(dateipfad) > self.zeitintervall:
                    self.ergebnis += [(dateipfad, time.ctime(getmtime(join(pfad, datei))))]


    def __str__(self):
        tabelle = ""

        for pfad, zeit in self.ergebnis:
            tabelle += str(pfad) + "\t" + str(zeit) + "\n"

        return SUCHBERICHT.format(tabelle)

wurzel = input("Wurzel des Verzeichnisbaums: ")
zeitintervall = input("Zeitintervall (Stunden)")

bot = Dateisuche(wurzel, zeitintervall)

print(bot)