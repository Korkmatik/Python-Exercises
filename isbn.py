#Dieses Program berechnet die Prüfziffer einer ISBN

ISBN = input("Geben Sie die ersten neun Ziffern ein: ") #Speichert die ersten neun Ziffern der ISBN

#berechnen der Prüfziffer
liste = list(ISBN)

s = 0
s += 1 * int(liste[0])
s += 2 * int(liste[1])
s += 3 * int(liste[2])
s += 4 * int(liste[3])
s += 5 * int(liste[4])
s += 6 * int(liste[5])
s += 7 * int(liste[6])
s += 8 * int(liste[7])
s += 9 * int(liste[8])

s = s % 11

#Ausgabe der Prüfziffer
print()
print("Prüfziffer:", s);
print()
input("ENTER zum Beenden")