import pickle

def suche(tel):
    """Diese Funktion sucht ob ein bestimmter Kontakt im Telefonbuch enthalten ist"""
    name = input("Name: ")
    if tel.get(name):
        print("Nummer:", tel.get(name), end='\n\n')
    else:
        print("Name unbekannt\n")

def neueNummer(tel):
    """Diese Funktion schreibt einen neuen Kontakt in das Telefonbuch"""
    # Eingabe des neuen Kontakts
    name = input("Name: ")
    nummer = input("Nummer: ")

    # Speichern des neuen Kontakts
    tel[name] = nummer
    
    file = open("tel.dmp", 'wb')
    pickle.dump(tel, file)
    file.close()

    print("Neuer Eintrag gespeichert\n")
    

def ausgabeNummern(tel):
    print("Name\t\t\tNummer")
    print(40 * "_")
    for i in tel.keys():
        print(i + "\t\t\t" + tel.get(i))
    print()

def beenden(tel  # Wörterbuch aus der die Daten kommen
            ):
    file = open("tel.dmp", 'wb')
    pickle.dump(tel, file)
    file.close()
    print("Danke, dass Sie dieses Produkt verwendet haben\n")

# Initialisieren der Anfangswerte
eingabe  = ""
telefonfile = open("tel.dmp", 'rb')
tel = pickle.load(telefonfile) # Schreiben des Telefonbuchs in ein Wörterbuch
telefonfile.close()

while eingabe != 'e':

    print("(S)uche nach Telefonnummer")
    print("(N)eue Nummer eintragen")
    print("(A)lle Nummern ausgeben")
    print("(E)nde\n")

    eingabe = input("Ihre Wahl: ")
    eingabe.lower()

    if eingabe == 's':
        suche(tel)
    elif eingabe == 'n':
        neueNummer(tel)
    elif eingabe == 'a':
        ausgabeNummern(tel)
    elif eingabe == 'e':
        continue
    else:
        print("Ungültige Eingabe!")

beenden(tel)
