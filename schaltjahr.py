# Dieses Programm liest eine Jahrezahl vom Benutzer ein
# und gibt aus, ob es sich um ein Schaltjahr handelt

eingabe = ""

while eingabe != -1:
	print("Geben Sie eine Jahreszahl ein. (-1 zum Beenden)")
	
	# Einlesen der Eingabe mit Fehlerbehandlung
	try:
		eingabe = int(input("Jahreszahl: "))
	except ValueError:
		print("Sie haben keine Ganzzahl eingegeben!\n")
	except:
		print("Ungültige Eingabe!\n")
	
	# Auswertung der Eingabe
	if eingabe == -1:
		continue
	elif (eingabe % 400 == 0) or (eingabe % 4 == 0 and eingabe % 100 != 0):
		print("Die Jahreszahl", eingabe, "ist ein Schaltjahr\n")
	else:
		print("Die Jahreszahl", eingabe, "ist kein Schaltjahr\n")