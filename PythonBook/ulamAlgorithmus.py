# Führt den Ulam Algormithmus aus

# Eingabe des Startwertes
print("Geben Sie einen Startwert ein.")
while True:
	try:
		a = float(input("Startwert: "))
		break
	except ValueError:
		print("Keine Zahl.")
	except:
		print("Ungültige Eingabe")
		
while a != 1.0:
	
	# Ist a gerade? -> dann folgt das..
	if (a % 2) == 0:
		a /= 2
	else:
		a = 3 * a + 1
	
	# Ausgabe aktuelles a
	print(a)