import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
laengeAlph = len(alphabet)

def verstecke(s,  # Erwartet einen String
              n=1 # Erwartet eine Intenger
              ):
    """Diese Funktion bekommt einen Text(s), dieser Text(s) wird
       verschlüsselt, indem nach jedem Zeichen eine beliebige Anzahl[n]
       von zufälligen Zeichen hinzugefügt wird"""
    verschluesselt = "" # hier wird der verschlüsselte Text gespeichert
    s = s.upper()
    
    for i in s:
        rand = random.randint(0, laengeAlph) # Zufällige Zahl um eine zufälligen
                                             # Buchstaben aus dem Alphabet auszuwählen
        
        verschluesselt += (i + n * alphabet[rand]) # Verschlüsselung

    return verschluesselt
