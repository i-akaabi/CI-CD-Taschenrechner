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
```
## Pipeline-Architektur

| Job | Zweck | Trigger / Bedingung | needs | Environment | Artifact |
|---|---|---|---|---|---|
| test | Dependencies installieren, Tests ausführen und Paket bauen | `push` und `pull_request` | - | - | erstellt `app-paket` |
| deploy | Artifact herunterladen und GitHub Release erstellen | nur Push auf `main` | `test` | `production` | verwendet `app-paket` |

## Pipeline im Überblick

Die CI/CD-Pipeline besteht aus zwei Jobs:

- `test`: installiert die Abhängigkeiten, führt die Pytest-Tests aus, erstellt ein ZIP-Paket und lädt dieses als Artifact hoch.
- `deploy`: startet nach erfolgreichem Test-Job, lädt das Artifact herunter und erstellt automatisch ein GitHub Release.

Die Jobs sind mit `needs: test` miteinander verbunden.

## Trigger

Der Workflow startet automatisch bei:

- `push`
- `pull_request`

Das Deployment wird nur bei einem Push auf den Branch `main` ausgeführt.

## Secrets und Environment

Für das Deployment wird das Environment `production` verwendet.

Verwendet werden:

- Secret: `DEPLOY_TOKEN`
- Variable: `DEPLOY_TARGET`

Der Wert des Secrets wird nicht im Repository oder im Log ausgegeben.

Das Environment ist auf den Branch `main` beschränkt.

## Deployment

Nach erfolgreichen Tests wird das erzeugte ZIP-Paket als Artifact an den Deployment-Job übergeben.

Bei einem Push auf `main` wird anschließend automatisch ein GitHub Release erstellt. Das erzeugte Paket wird dem Release als Datei hinzugefügt.

## Lokal ausführen

Virtuelle Umgebung erstellen:

```bash
python3 -m venv .venv
```

Aktivieren:

```bash
source .venv/bin/activate
```

Abhängigkeiten installieren:

```bash
python -m pip install -r requirements.txt
```

Tests ausführen:

```bash
python -m pytest -v
```

Paket lokal erstellen:

```bash
mkdir -p build
python -m zipfile -c build/app-paket.zip src/
```

## Abschluss-Challenge

Bei der fehlerhaften Beispiel-Pipeline wurden folgende Probleme erkannt und korrigiert:

1. Python-Version als String festlegen.
2. Dependencies vor den Tests installieren.
3. Richtigen Dateinamen `requirements.txt` verwenden.
4. Repository im Job auschecken und Jobs mit `needs` verbinden.
5. Deployment auf `main` beschränken und Secrets nicht ausgeben.
6. Cache-Key mit `hashFiles('requirements.txt')` erstellen.

## Ergebnis

Die Anwendung wird automatisch getestet, gebaut und als Artifact weitergegeben. Nach erfolgreichen Tests wird auf `main` automatisch ein GitHub Release erstellt.