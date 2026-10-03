# CI-CD-Taschenrechner

## Was macht das Projekt?

Dieses Projekt ist eine kleine Python-Taschenrechner-Bibliothek und dient als Beispiel für eine vollständige CI/CD-Pipeline mit GitHub Actions.

Die Anwendung enthält Funktionen für Addition, Durchschnittsberechnung und Prozentrechnung. Die Funktionen werden automatisch mit Pytest getestet.

## Projektstruktur

```text
CI-CD-Taschenrechner/
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── src/
│   ├── __init__.py
│   └── rechner.py
├── tests/
│   └── test_rechner.py
├── .gitignore
├── requirements.txt
└── README.md