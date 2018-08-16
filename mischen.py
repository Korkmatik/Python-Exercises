import random

def erstellen():
    farben = ['Kreuz', 'Pik', 'Herz', 'Karo']
    werte = ['Ass', 'König', 'Dame', 'Bube', 'Zehn', 'Neun', 'Acht', 'Sieben']
    karten = []
    
    for i in range(len(farben)):
        for j in range(len(werte)):
            karten.append((farben[i], werte[j]))

    return karten

def mischen(anzahl, # Wie oft gemischt werden soll (Integer)
            liste   # Liste die durchgemischt werden soll
            ):
    temp = []
    for i in range(anzahl):
        rand1 = random.randint(0, len(liste)-1)
        rand2 = random.randint(0, len(liste)-1)

        temp.append(liste[rand1])
        liste[rand1] = liste[rand2]
        liste[rand2] = temp[0]
        temp.clear()

    return liste
        
