from os.path import join, normcase
from os import walk

SUCHBERICHT = """
 Suchbericht
 -----------
 {}
 Es wurden {} Dateien durchsucht.
 {} Dateien waren nicht lesbar.
 """

class Suchroboter:
    def __init__(self, suchwort, wurzel):
        self.ergebnis = []
        self.suchwort = suchwort
        self.wurzel = wurzel
        self.nicht_lesbar = 0
        self.durchsucht = 0
        liste = walk(wurzel)

        for pfad, verzeichnis, dateien in liste:
            for datei in dateien:
                self.durchsucht += 1
                try:
                    f = open(join(pfad, datei), 'r')
                    text = f.read()
                    f.close()
                    n = text.count(suchwort)
                    if n > 0:
                        p = normcase(join(pfad, datei))
                        self.ergebnis += [(n, p)]
                except:
                    self.nicht_lesbar += 1

        self.ergebnis.sort(reverse=True)
        
    def __str__(self):
        tabelle =""
        for (n, pfad) in self.ergebnis:
            tabelle += "{} ({} Vorkommen)\n".format(pfad, n, self.suchwort)
        
        return SUCHBERICHT.format(tabelle, self.durchsucht, self.nicht_lesbar)

# Hauptprogramm
suchwort = input("Suchwort: ")
wurzel = input("Wurzelverzeichnis: ")
bot = Suchroboter(suchwort, wurzel)

print(bot)    