class NieprawidlowyWiek(Exception):
    pass

try:
    wiek = -5
    if wiek < 0:
        raise NieprawidlowyWiek("Wiek nie może być ujemny")
except NieprawidlowyWiek as e:
    print(f"Błąd: {e}")