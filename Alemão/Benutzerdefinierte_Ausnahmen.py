class UngueltigesAlter(Exception):
    pass

try:
    alter = -5
    if alter < 0:
        raise UngueltigesAlter("Alter kann nicht negativ sein")
except UngueltigesAlter as e:
    print(f"Fehler: {e}")