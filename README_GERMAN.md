# Tag 10 - Taschenrechner 🧮

In diesem Projekt wurde ein einfacher Taschenrechner programmiert, der dem Benutzer ermöglicht, fortlaufende Berechnungen mit vorherigen Ergebnissen durchzuführen. 

## Funktionen

- Grundrechenarten: Addition, Subtraktion, Multiplikation, Division
- Nutzung von Funktionen und Dictionaries zur Operationserkennung
- Wiederverwendung von Ergebnissen für weitere Rechnungen
- ASCII-Art-Logo (`art.py`)

## Funktionsweise

- Benutzer gibt eine erste Zahl ein.
- Benutzer wählt einen Rechenoperator (`+`, `-`, `*`, `/`).
- Benutzer gibt eine zweite Zahl ein.
- Das Ergebnis wird angezeigt.
- Benutzer entscheidet, ob er mit dem Ergebnis weiterrechnen oder neu starten möchte.

## Beispielausgabe
```
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

Enter the first number: 13
+
-
*
/
Pick an operation: *
Enter the next number: 24
13.0 * 24.0 = 312.0
Type 'y' to continue calculating with 312.0, or type 'n' to start a new calculation:
```

## Gelernt

- Funktionen mit Rückgabewerten schreiben
- Mehrere Werte zurückgeben
- Funktionen in Dictionaries speichern
- Schleifen und Logik zur Steuerung des Programms
- Docstrings verwenden
- Einfache Benutzerführung mit ASCII-Art gestalten
- Verschiedene Syntax Möglichkeiten für Boolean-Logik: `again = yes_no == "y"`
