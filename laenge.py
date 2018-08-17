class Laenge:
    """Dieses Klasse dient der Repräsentation von Strecken
       Attribute: betrag(Speichert den Betrag der Länge), einheit(Speichert die Einheit des Objekts)
       Methoden: getMeter()
       Überladungen: __add__(), __gt__(), __ge__(), __eq__(), __str__()"""

    # Beinhaltet zur jeweiligen Einheit die Umrechnung in Meter
    __meter = {'mm': 0.001, 'cm': 0.01, 'm': 1, 'km': 1000, 
                'in': 0.0254, 'ft': 0.3048, 'yd': 0.9143, 'mil': 1609}
    
    def __init__(self, betrag, einheit):
        self.betrag = float(betrag)
        self.einheit = einheit

    def getMeter(self):
        return self.betrag * self.__meter[self.einheit]

    def __add__(self, laenge):
        a = self.getMeter()
        b = laenge.getMeter()
        summe = a + b
        summe = summe * self.__meter[self.einheit]
        return Laenge(summe, self.einheit)

    def __gt__(self, laenge):
        return self.getMeter() > laenge.getMeter()

    def __ge__(self, laenge):
        return self.getMeter() >= laenge.getMeter()

    def __eq__(self, laenge):
        return self.getMeter() == laenge.getMeter()

    def __str__(self):
        return format(self.betrag, '.2f') + ' ' + self.einheit
    
# Testumgebung
if __name__ == '__main__':
    s1 = Laenge(40, 'm')
    s2 = Laenge(1, 'km')

    print('s1 < s2:', s1 < s2)
    print('s1 + s2:', s1 + s2)
    s1 += s2
    print('s1 < s2:', s1 < s2)
    print(s1, s2, sep='\n')
