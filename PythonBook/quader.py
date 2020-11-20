from ding import Ding

class Quader(Ding):
    """Diese Klasse beschreibt einen Quader aus einem bestimmten Material, sie erbt von Ding
       Attribute: __lenge, __breite, __hoehe, diese beschreiben die Ausmaße eines Quaders in cm
       Methoden: Überladen der Vergleichsoperatoren: ==, >, >=
       Überschreiben der Methode aus Din: __str__()"""
    
    def __init__(self, symbol, laenge, breite, hoehe):
        Ding.__init__(self, symbol, laenge*breite*hoehe/100)
        self.__laenge = float(laenge)
        self.__breite = float(breite)
        self.__hoehe = float(hoehe)
    
    def __str__(self):
        return "Dies ist ein Quader aus " + self._dichte[self._symbol][0] + "\nAusmaße:\nLänge: " + self.__laenge + \
                "\nBreite: " + self.__breite + "\nHöhe: " + self.__hoehe

    def __gt__(self, quader):
        return self.getMasse() > quader.getMasse()

    def __ge__(self, quader):
        return self.getMasse() >= quader.getMasse()

    def __eq__(self, quader):
        return self.getMasse() == quader.getMasse()
