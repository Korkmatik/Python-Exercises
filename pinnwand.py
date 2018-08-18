import pickle

class Pinnwand():
    """Dies ist eine Klasse um Notizen zu verwalten"""

    def __init__(self):
        # Schreibt sämtliche Notizen in den Arbeitsspeicher
        try:
            file = open("pinnwand.dmp", 'rb')
        except FileNotFoundError:
            print("Datei konnte nicht gefunde werden. Erstelle Datei...")
            """file = open("pinnwand.dmp", 'w')
            file.close()
            file = open("pinnwand.dmp", 'rb')"""
        try :
            self.__notizen = pickle.load(file)
        except: 
            self.__notizen = []
        file.close()

    def __ermittlePrioritaet(self, notiz):
        notiz = str(notiz)
        return notiz.count('!') + notiz.upper().count('WICHTIG') + notiz.upper().count('EILIG') + notiz.upper().count('DRINGEND')
    
    def hefteAn(self):
        """Diese Methode speichert eine beliebige Anzahl von Notizen in einer Datei"""
        f = open("pinnwand.dmp", 'wb')
        eingabe = "-"

        # Eingabe der Notizen vom Benutzer
        while eingabe != "":
            eingabe = input("Notiz: ")
            self.__notizen.append((self.__ermittlePrioritaet(input), input))

        # Sortieren der Notizen nach Prioriät
        self.__notizen.sort()
        self.__notizen.reverse()

        # Schreiben der Notizen auf die Festplatte
        pickle.dump(self.__notizen, f)

        # Speichern der Daten
        f.close()

    def __str__(self):
        message = "Notizen\n"

        for msg in self.__notizen:
            message += "{notiz} (Priorität: {prio})\n".format(notiz=msg[1], prio=msg[0])

        return message

    def entferne(self):
        """Entfernt die Notiz mit der höchsten Priorität und gibt die Notiz aus"""
        
        f = open("pinnwand.dmp", 'wb')
        notiz = self.__notizen[0][0] # Speichern der wichtigsten Notiz um sie später auszugeben

        del self.__notizen[0] # Wichtigste Notiz wird gelöscht

        # Abspeichern der Notizen auf der Festplatte
        pickle.dump[self.__notizen, f]

        f.close()

        return notiz + '\n'