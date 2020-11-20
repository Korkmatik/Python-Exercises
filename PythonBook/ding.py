class Ding:

    _dichte = {'Fe': ('Eisen', 7.87), 'Au': ('Gold', 19.32), 'Ag': ('Silber', 10.5)}
    
    def __init__(self, symbol, volumen):
        self._symbol = symbol
        self.__volumen = float(volumen)
        self.__masse = float(self.__volumen * self._dichte[symbol][1])

    def getMasse(self):
        """Liefert die Masse in Gramm"""
        return self.__masse

    def getVolumen(self):
        """Liefert das Volumen in Kubikzentimeter"""
        return self.__volumen

    # Überschreiben der __str__()-Methode
    def __str__(self):
        return 'Symbol: ' + self._symbol + '\nElement: ' + self._dichte[self._symbol][0] \
        + '\nVolumen: ' + format(self.getVolumen(), '.2f') + ' ccm' + '\nMasse: ' + format(self.getMasse(), '.2f') + ' g' \
        + '\nDichte: ' + format(self._dichte[self._symbol][1]) + ' g/ccm'
