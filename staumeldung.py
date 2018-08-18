import random

class Staumeldung:
    """Diese Klasse formuliert Staumeldungen"""

    def __init__(self, informationen = ('Autobahn', 'Richtung', 'Abfahrt/Autobahnkreuz', 0) # Information ist ein Tupel aus: Autobahn, Richtung, Abfahrt/Autobahnkreuz, Länge des Staus in km
                ):
        
        self.__informationen = informationen

    def __str__(self):
        rand = random.randint(0, 20)

        if rand < 10:
            meldung = "Ein Stau von {laenge} km Länge erwartet Sie auf der {autobahn} Richtung {richtung} vor dem\n".format(laenge=self.__informationen[3], \
                                                                                                        autobahn=self.__informationen[0], richtung=self.__informationen[1])
            meldung += "{abfahrt}. {abfahrt}.\n".format(abfahrt=self.__informationen[2])
        else:
            meldung = "Auf der {autobahn} Richtung {richtung} vor der Abfahrt {abfahrt} {laenge} km Stau".format(autobahn=self.__informationen[0], richtung=self.__informationen[1], \
                                                                                                        abfahrt=self.__informationen[2], laenge=self.__informationen[3])

        return meldung


if __name__ == "__main__":
    stau1 = Staumeldung(('A1', 'Köln', 'Westhofener Kreuz', 6))
    stau2 = Staumeldung(('A40', 'Bochum', 'Bochum Zentrum', 4))
    stau3 = Staumeldung(('A40', 'Bochum', 'Bochum Zentrum', 4))
    stau4 = Staumeldung(('A40', 'Bochum', 'Bochum Zentrum', 4))

    print(stau1, stau2, stau3, stau4, sep='\n')