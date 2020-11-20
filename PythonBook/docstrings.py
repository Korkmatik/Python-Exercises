import re

def sucheWoerter(text, n):
    """
    >>> sucheWoerter("Wepus ist ein haariger Bursche", 3)
    ['ist', 'ein']
    >>> text = "Habe nun, ach! Philosphie, Juristerei und Medizin und leider auch Theologie durchaus studiert, mit heißem Bemühn."
    >>> sucheWoerter(text, 4)
    ['Habe', 'auch']"""

    text = re.sub('[.,;:!@#$]', '', text)
    words = text.split()
    result = []

    for w in words:
        if len(w) == n: 
            result.append(w)

    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)