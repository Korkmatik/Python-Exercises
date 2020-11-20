def konkat(*text):
    """Diese Funktion bekommt eine beliebige Anzahl
       von Text und konkateniert diesen Text""" 
    gesamt = ""
    for i in text:
        gesamt += i;
    return gesamt
