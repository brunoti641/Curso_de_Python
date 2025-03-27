# 6. Fehlerbehandlung und Ausnahmen
try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    print("Division durch Null nicht erlaubt!")
finally:
    print("Aufräumen...")

# Eigene Ausnahme
class MeineAusnahme(Exception):
    pass

raise MeineAusnahme("Ein benutzerdefinierter Fehler")