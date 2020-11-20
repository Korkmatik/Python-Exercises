# Dieses Programm gibt die Vermehrung von Bakterien für die ersten zwei Tage aus (100 Exemplare am Anfang, Ausgabe aktuelle Anzahl pro Stunde)

print("Vermehrung von Bakterien")

stunden = 0
bakterien = 100

while stunden <= 48:
	print("Stunde", stunden, "  ", bakterien, "Bakterien")
	bakterien *= 4
	stunden += 1