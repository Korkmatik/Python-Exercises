def haeufigkeit(string # Bekommt eine String zu dem die Häufigkeit der Buchstaben ausgegeben werden soll
               ):
    """Funktion gibt die Häufigkeit der Buchstaben in einem String aus"""
    d = {}
    for i in string:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1

    return d
