import pickle

# def suche():

# def neueNummer():

# def ausgabeNummern():

def beenden(datei, # File in die Daten des Wörterbuchs geschrieben werden soll
            dic    # Wörterbuch aus der die Daten kommen
            ):
    pickle.dump(dic, datei)
    datei.close()
    

def initialisieren(tel, # Bekommt ein Dictionary in das die Daten geladen werden
                   ):
    """Hier werden sämtliche Vorkehrungen getroffen, bevor das Programm vom
       Benutzer benutzt werden darf
       Aufgaben: Telefonbuch öffnen
                 Daten in Wörterbuch schreiben
       Rückgabetyp: FILE"""
    try:
        file = open("tel.dmp", 'rb')
    except FileNotFoundError:
        print("Telefonbuch existiert nicht")

    eingabe = ""
    tel = pickle.load(file)

    return file

tel = {}
file = initialisieren(tel)

while eingabe != 'e':

    print("(S)uche nach Telefonnummer")
    print("(N)eue Nummer eintragen")
    print("(A)lle Nummern ausgeben")
    print("(E)nde")

    eingabe = input("Ihre Wahl: ")
    eingabe.lower()

    if eingabe == 's':
        #suche()
    #elif eingabe == 'n':
        #neueNummer()
    #elif eingabe == 'a':
        #ausgabeNummern()
    else:
        print("Ungültige Eingabe!")

beenden()
