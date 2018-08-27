from schlange import Queue

MENU = """
(N)euer Kunde
(A)bfertigen des nächsten Kunden
(E)nde
"""

class Userinterface:
    def __init__(self):
        self.__queue = Queue()

        self.__initUI()
        

    def __initUI(self):
        print("Warten beim TÜV")
        print(MENU)
        inp = input("Auswahl: ")

        while True:
            if inp in 'nN':
                self.__newCustomer()
            elif inp in 'aA':
                self.__nextCustomer()
            elif inp in 'eE':
                if self.__queue.empty():
                    print('Ich wünsche einen schönen Feierabend!')
                    break
                else:
                    print('Es warten noch Kunden!')                                
            else:
                print('Ungültige Eingabe!')

            print(MENU)
            inp = input("Auswahl: ")

    def __newCustomer(self):
        customer = input("Kennzeichen: ")
        self.__queue.enqueue(customer)
    
    def __nextCustomer(self):
        customer = self.__queue.dequeue()
        print("Der nächste Kunde ist: " + customer)

Userinterface()