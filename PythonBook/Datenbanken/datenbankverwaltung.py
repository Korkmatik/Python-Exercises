import sqlite3
from threading import Thread

MENU = """Was möchten Sie machen?
(N)euer Eintrag
(A)usgabe der Tabelle
(E)nde"""

class Admin:
    def __init__(self, db, table):
        
        print(19 * "-")
        self.db = db
        self.table = table
        
        self.__runProgram()

    def __runProgram(self):        
        print("Datenbankverwaltung")
        print(MENU)
        self.input = input("Eingabe: ")

        while not (self.input in 'eE'):
            if self.input in 'nN':
                self.__newEntry()
            elif self.input in 'aA':
                self.__showDb()
            elif self.input in 'eE':
                continue
            else:
                print("Eingabe unbekannt")
            
            print("\n" + MENU)
            self.input = input("Eingabe: ")

    def __newEntry(self):
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()

        name = input("Name: ")
        table = cursor.execute("""SELECT * from {} WHERE name = "{}";""".format(self.table, name))
        try:    
            if name in list(table)[0]:
                print("Fehler: Name existiert schon!")
                return -1
        except:
            tel = input("Telefonnummer: ")

            cursor.execute("""INSERT INTO {} VALUES("{}", "{}")""".format(self.table, name, tel))
            connection.commit()
            connection.close()

            print(name + " " + tel + " wurden in der Datenbank " + self.db + "in die Tabelle " + self.table + " geschrieben")
            return 0

    def __showDb(self):
        """Shows the Database in a Table-Format"""
        connection = sqlite3.connect(self.db)
        cursor = connection.cursor()
        table = list(cursor.execute("""SELECT * FROM {};""".format(self.table)))

        print("Name" + 16 * " " + "| Telefonnummer")
        print(20 * "-" + "|" + 14 * "-")
        for item in table:
            print("{:<20}| {}".format(item[0], item[1]))


Admin("test.db", "person")