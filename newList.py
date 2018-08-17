class NewList(list):

    def __init__(self, liste=[]):
        list.__init__(self, liste)

    def range(self):
        return max(self) - min(self)