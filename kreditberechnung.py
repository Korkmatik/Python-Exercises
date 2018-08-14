# Dieses Programm berechnet den zu zahlenden Betrag nach Kreditaufnahme

# Variablen
tilgung = 0.0
restschulden = 0.0
zinsen = 0.0
jahr = 2018

# Eingabe der Daten
print("Kreditberechnung")

while True:
	try:
		kreditsumme = float(input("Kreditsumme in Euro: "))
		zinssatz = float(input("Zinssatz (Prozent pro Jahr): "))
		rueckzahlung = float(input("Jährliche Rückzahlung in Euro: "))
		break
	except ValueError:
		print("Sie haben keine Zahl eingegeben")
	except:
		print("Ungültige Eingabe")
		
print()

restschulden = kreditsumme

while rueckzahlung < restschulden:

	zinsen = restschulden * (zinssatz / 100) # Berechnung der aktuellen Zinsen
	tilgung = rueckzahlung - zinsen # Berechnung der aktuellen Tilgung
	restschulden -= tilgung # Berechnung der aktuellen Restschulden

	print(jahr, "Zinsen:", zinsen, "EUR  Tilgung:", tilgung, "EUR  Restschulden:", restschulden, "EUR") # Ausgabe
	jahr += 1
	
# Ausgabe der Restforderung da diese kleiner als die jährliche Rückzahlung ist
print("Restforderung:", restschulden, "EUR\n")
input("ENTER zum beenden")