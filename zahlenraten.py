# Dieses Programm ist ein kleines Spiel, indem eine Zufällige Zahl zwischen 0 und 100 erzeugt wird
# und der Benutzer diese erraten muss

import random

eingabe = 101

while eingabe != -1:

	#random Zahl erzeugen
	z = random.randint(0, 100)
	print("Bitte geben Sie ein Zahl zwischen 0 und 100 ein. (-1 zum Beenden)")
	
	while eingabe != -1:
		
		# Einlesen der Eingabe des Benutzers mit Fehlerbehandlung
		try:
			eingabe = int(input("Zahl: "))
		except ValueError:
			print("Sie habe keine Zahl eingegeben\n")
		except:
			print("Ungültige Eingabe\n")
			
		# Auswertung der Eingabe
		if eingabe == -1:
			print("Beende...")
			break
		elif eingabe < z:
			print("Zu klein!")
		elif eingabe > z:
			print("Zu groß!")
		elif eingabe == z:
			print("Herzlichen Glückwunsch! Sie habe die Zahl gefunden\n")
			break