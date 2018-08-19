from re import *

class Lesbarkeit:
    def __init__(self, datei):
        f = open(datei, 'r')
        self.text = f.read()
        f.close()

    def anzahlWoerter(self):
        return len(self.text.split())

    def anzahlSaetze(self):
        re = compile('[!?.,;:]' + '\s')
        return len(re.split(self.text))

    def anzahlSilben(self):
        re = compile('[aeiou]+', I)
        return len(re.split(self.text))

    def readability(self):
        asl = float(self.anzahlWoerter()) / self.anzahlSaetze()
        asw = float(self.anzahlSilben()) / self.anzahlWoerter()
        return int(206.835 - 1.015 * asl - 84.6 * asw)

    def __str__(self):
        return 'Lesbarkeitsindex nach Flesch: ' + \
                str(self.readability())

print(Lesbarkeit('test.txt'))      