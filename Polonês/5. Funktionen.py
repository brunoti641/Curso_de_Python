# 5. Funktionen
# Funktionen sind wiederverwendbare Codeblöcke, die spezifische Aufgaben kapseln. Sie machen Code modularer und wartbarer.

def begruessung():
    print("Hallo, Welt!")

def addiere(a, b):
    return a + b

quadrat = lambda x: x ** 2

# Docstrings Beispiel
def flaeche_rechteck(laenge, breite):
    """
    Berechnet die Fläche eines Rechtecks.
    
    Args:
        laenge (float): Länge des Rechtecks.
        breite (float): Breite des Rechtecks.
    
    Returns:
        float: Fläche des Rechtecks.
    """
    return laenge * breite