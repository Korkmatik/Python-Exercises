z = 1 # Näherungswert

def wurzel(x,    # Zahl dessen Wurzel berechnet werden soll
           n=10  # Anzahl der Näherungen
           ):
    """Diese Funktion berechnet die Wurzel der Zahl x mit dem heronschen Verfahren
       Rückgabe: float"""

    if n <= 0:
        return 1
    else:
        return 0.5 * ( wurzel(x, n-1) + x/wurzel(x, n-1))
