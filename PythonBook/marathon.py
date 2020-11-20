import time

def modifiziereDaten(daten):
    """Fügt die aktuelle Uhrzeit vor die Startnummer ein"""
    zeit = time.asctime()
    daten = str(zeit) + "\t" + daten + "\n"
    return daten

def schreibeDaten(file, daten):
    """Schreibt die Übergegeben Daten in die Datei"""
    if not file.closed:
        file.write(daten)
        file.flush()
    else:
        print('Fehler: Datei ist nicht geoeffnet!')
        
        
# Öffnen der Datei
try:
    pfad = "marathon\\daten.txt"
    daten = open(pfad, 'w')
except:
    print('Datei konnte nicht geoeffnet werden')
    

# Eingabe des Benutzeres
eingabe = input("Startnummer: ")

while eingabe:
    
    eingabe = modifiziereDaten(eingabe)
    schreibeDaten(daten, eingabe)
    eingabe = input("Startnummer: ")

print('\nDie Daten befinden sich in der Datei ' + pfad)
daten.close()
