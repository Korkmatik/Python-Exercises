import os

vorname = input("Vorname: ")
nachname = input("Nachname: ")

verzeichnis = ('user/' + vorname + ' ' + nachname).lower()

os.mkdir(verzeichnis)