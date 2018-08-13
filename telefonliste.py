#Dieses Programm liest dreimal Name und Telefonnummer ein und gibt diese wieder aus

#eingabe der Daten
print("Bitte geben Sie Name und Telefonnummer ein")

kontakt1 = (input("Name: "), input("Telefonnummer: "))
kontakt2 = (input("Name: "), input("Telefonnummer: "))
kontakt3 = (input("Name: "), input("Telefonnummer: "))

telefonliste = [kontakt1, kontakt2, kontakt3]

#ausgabe der Telefonliste
print("Telefonliste: ")
print(telefonliste[0][0], telefonliste[0][1])
print(telefonliste[1][0], telefonliste[1][1])
print(telefonliste[2][0], telefonliste[2][1])
input("ENTER zum beenden")