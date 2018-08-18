import pickle

class Pinnwand():
    """Dies ist eine Klasse um Notizen zu verwalten"""

    def __init__(self):
        # Schreibt sämtliche Notizen in den Arbeitsspeicher
        try:
            file = open("pinnwand.dmp", 'rb')
        except FileNotFoundError:
            print("Datei konnte nicht gefunde werden. Erstelle Datei...")
            file = open("pinnwand.dmp", 'w')
            file.close()
            file = open("pinnwand.dmp", 'rb')
        self.__notizen = pickle.load(file)
        file.close()

        # Benutzeroberfläche
        print("Pinnwand")
        self.__message = '(N)eue Notiz anheften'.ljust(30) + '(A)lle Notizen auflisten\n' + \
                         '(W)ichtigeste Notiz entfernen'.ljust(30) + '(E)nde'
        __run()

    def __run():
        while True:
            input = input("Ihre Wahl: ")

            if input in 'nN':
                hefteAn()
            elif input in 'aA':
                print(self)
            elif input in 'wW':
                entferne()
            elif input in 'eE':
                break
            else:
                print('Ungültige Eingabe')

    def __ermittlePrioritaet(self, notiz):
        return notiz.count('!') + notiz.upper().count('WICHTIG') + notiz.upper().count('EILIG') + notiz.upper().count('DRINGEND')
    
    def hefteAn(self):
        """Diese Methode speichert eine beliebige Anzahl von Notizen in einer Datei"""
        f = open("pinnwand.dmp", 'wb')

        while input != "":
            input = input("Notiz: ")
            
        