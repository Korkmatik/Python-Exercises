# Dieses Programm liest das Alter vom Benutzer ein und gibt aus, ob es sich nach deutschem Recht um einen Jugendlichen handelt

while True:
	try:
		print("Bitte geben Sie ihr Alter ein")
		alter = int(input("Alter: "))
		break
	except ValueError:
		print("Sie haben keine Zahl eingegen")
	except:
		print("Ungültige Eigabe")
	
# Verarbeiten der Angabe des Benutzers	
if 14 < alter < 18:
	print("Sie sind nach deutschem Recht ein Jugendlicher.")
else:
	print("Sie sind nach deutschem Recht kein Jugendlicher.")
	
input("ENTER zum beenden")