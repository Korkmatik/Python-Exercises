import os
import re

class Suchroboter:
    def __init__(self, wort, wurzel):
        self.__wort = wort
        self.__wurzel = wurzel
        self.__pfade = {}

        self.__suche()

    def __suche(self):
        dateien = os.walk(self.__wurzel)
        re = compile('[.,:;?!]' + '\s')

        for pfad, unterverzeichnis, datei in dateien:
                f = open(datei, 'r')
                liste = f.read()
                f.close()
                re.split(liste) # zerlegen der liste in einzelne wörter

                for self.__wort in liste:
                    if self.__pfade.get(os.path.join(pfad, datei)):
                        self.__pfade[os.path.join(pfad, datei)] += 1
                    else:
                        self.__pfade = {str(os.path.join(pfad, datei)): 1}

    def __str__(self):
        bericht = 'Suchbericht\n' + 11*'-' + '\n'
        bericht += 'Suchbegriff: {wort}\nWurzel des Verzeichnisbaums: {wurzel}\n\n'.format(wort=self.__wort, wurzel=self.__wurzel)

        for i in self.__pfade.keys():
            bericht += '{pfad} ({vorkommen} Vorkommen)'.format(pfad=i, vorkommen=self.__pfade[i])

        return bericht