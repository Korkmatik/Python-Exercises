def mengeRechtwinkligeDreiecke():
    dreiecke = set()

    for a in range(1, 20):
        for b in range(1, 20):
            for c in range(1, 20):
                if(a**2 + b**2) == c**2:
                    dreiecke.add(frozenset(a, b, c))

    return len(dreiecke)
