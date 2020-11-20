# Gibt sämtliche Basenpaare aus den folgenden Basen aus

basen = ["AT", "TA", "GC", "CG"]

for a in basen:
	for b in basen:
		for c in basen:
			for d in basen:
				print(a, b, c, d)