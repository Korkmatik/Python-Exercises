from pinnwand import Pinnwand

class Benutzeroberflaeche:
    __message = '(N)eue Notiz anheften'.ljust(35) + '(A)lle Notizen auflisten\n' + \
                '(W)ichtigeste Notiz entfernen'.ljust(35) + '(E)nde'

    def __init__(self, pinnwand):
        self.__pw = pinnwand
        print("Pinnwand")

    def run(self):
        while True:
            print(self.__message)
            eingabe = input("Ihre Wahl: ")

            if eingabe in 'nN':
                self.__pw.hefteAn()
            elif eingabe in 'aA':
                print(self.__pw)
            elif eingabe in 'wW':
                print(self.__pw.entferne())
            elif eingabe in 'eE':
                break
            else:
                print('Ungültige Eingabe')



if __name__ == '__main__':
    pw = Pinnwand()
    ben = Benutzeroberflaeche(pw)
    ben.run()