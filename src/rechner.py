# ----------------------------------------------------
# Kleine Taschenrechner-Bibliothek
# ----------------------------------------------------
# Diese Datei enthält einfache mathematische Funktionen.
# Sie wird später durch automatisierte Tests geprüft.
# ----------------------------------------------------


def summe(a, b):
    """
    Addiert zwei Zahlen und gibt das Ergebnis zurück.
    """
    return a + b


def durchschnitt(zahlen):
    """
    Berechnet den Durchschnitt einer Liste von Zahlen.
    """
    if not zahlen:
        return 0

    return sum(zahlen) / len(zahlen)


def prozent(anteil, gesamt):
    """
    Berechnet, wie viel Prozent ein Anteil vom Gesamtwert ist.
    """
    if gesamt == 0:
        return 0

    return (anteil / gesamt) * 100