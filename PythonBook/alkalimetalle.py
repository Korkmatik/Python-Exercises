# Dieses Programm bekommt die Formel eines chemischen Elements vom Benutzer
# und gibt aus, ob es sich um ein Alkalimetall handelt

alkali = ["Li", "Na", "K", "Rb", "Cs"]
eingabe = ""

while eingabe != "q":
	print("Bitte geben Sie die Formel eines chemischen Elementes an. (q = Beenden)")
	try:
		eingabe = input("Element: ")
	except:
		print("Ungültige Eingabe!\n")
	
	# Verarbeitung der Eingabe
	if eingabe == "q":
		continue
	elif eingabe in alkali:
		print("Es handelt sich um ein Alkalimetall.\n")
	else:
		print("Es handelt sich nicht um ein Alkalimetall\n")