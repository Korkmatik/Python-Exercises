print("Kostenplan für eine Reise")
print("-------------------------")

kostenReisebus = input("Kosten für den Reisebus: ")
hotelkosten = input("Hotelkosten pro Person: ")
gesamtkostenEvents = input("Gesamtkosten für touristische Events: ")
teilnehmer = input("Anzahl der Teilnehmer: ");

gesamtkosten = float(kostenReisebus) + float(hotelkosten) * int(teilnehmer) + float(gesamtkostenEvents)
kostenProPers = gesamtkosten / int(teilnehmer)

print("Die Gesamtkosten betragen", gesamtkosten, "EUR")
print("Die Kosten pro Person sind", kostenProPers, "EUR")

input()
