# ----------------------------------------------------
# Automatisierte Tests für die Taschenrechner-Bibliothek
# ----------------------------------------------------
# Pytest führt diese Tests später lokal und automatisch
# über die GitHub-Actions-Pipeline aus.
# ----------------------------------------------------

from src.rechner import summe, durchschnitt, prozent


# ----------------------------------------------------
# Test für die Addition
# ----------------------------------------------------
def test_summe():
    assert summe(2, 3) == 5


# ----------------------------------------------------
# Test für die Durchschnittsberechnung
# ----------------------------------------------------
def test_durchschnitt():
    assert durchschnitt([2, 4, 6]) == 4


# ----------------------------------------------------
# Test für die Prozentberechnung
# ----------------------------------------------------
def test_prozent():
    assert prozent(25, 100) == 25


# ----------------------------------------------------
# Sonderfall: leere Liste
# ----------------------------------------------------
def test_durchschnitt_leere_liste():
    assert durchschnitt([]) == 0


# ----------------------------------------------------
# Sonderfall: Division durch null vermeiden
# ----------------------------------------------------
def test_prozent_gesamt_null():
    assert prozent(25, 0) == 0