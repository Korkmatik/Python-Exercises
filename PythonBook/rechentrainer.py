# Dies ist ein Rechentrainer

import random
import time

print("Multiplikationstrainer")
print("----------------------")

# Zeitmessung
start = time.time()

for i in range(5):

	# Aufgabe
	a = random.randint(0, 10)
	b = random.randint(0, 10)
	
	ergebnis = a * b	
	
	eingabe = -1
	
	# Eingabe des Benutzers
	while eingabe != ergebnis:
		
		eingabe = int(input(str(a) + " * " + str(b) +	" = "))
		
		if eingabe != ergebnis:
			print("Falsch! Versuchen Sie es noch einmal!")
		else:
			print("Richtig!")

# Zeitmessung
ende = time.time()
diff = int(ende - start)

print("Für die Aufgabe habe Sie", diff, "Sekunden benötigt")