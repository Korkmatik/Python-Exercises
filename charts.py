#Dieses Program liest 3 Titel ein und gibt sie aus

#einlesen der Charts
print("Bitte geben Sie die ersten Titel der Charts ein!")

charts = []
charts.append(input("Title: "))
charts.append(input("Title: "))
charts.append(input("Title: "))

#ausgabe der Charts
print("Hier sind die ersten drei Titel der Charts: ")
print("Platz 1: " + charts[0])
print("Platz 2: " + charts[1])
print("Platz 3: " + charts[2])
print()
input("ENTER zum beenden")