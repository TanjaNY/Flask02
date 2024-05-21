
# Eine Flask-Anwendung erstellen

# Flask02
Das ist die zweite Flask-Lektion, die erste Lektion findest du hier:https://github.com/TanjaNY/Flask


## 1.Hinzufügen einer Datenbank zur Anwendung
Wir haben eine Web-Anwendung erstellt. Jetzt möchten wir alle Ergebnisse speichern. Dafür benötigen wir eine Datenbank. Wir werden SQLite verwenden.

## Was ist SQLite?
SQLite ist ein leichtgewichtiges, serverloses Datenbankmanagementsystem, das auf einer einzigen Datei basiert. Es bietet eine vollständige SQL-Unterstützung und ist eine einfache Lösung für die Speicherung und Verwaltung von Daten in Anwendungen.

## Warum ist SQLite für eine kleine und leichte Flask-Anwendung geeignet?
Es gibt mehrere Gründe, warum SQLite für eine kleine und leichte Flask-Anwendung geeignet ist:

- **Einfache Integration:** SQLite kann problemlos in Python-Anwendungen wie Flask integriert werden. Es gibt verschiedene Python-Bibliotheken, die die Interaktion mit SQLite-Datenbanken vereinfachen, wie zum Beispiel sqlite3 oder SQLAlchemy.
- **Kein zusätzlicher Server erforderlich:** Da SQLite serverlos ist, benötigen Sie keinen zusätzlichen Datenbankserver, der separat installiert und verwaltet werden muss. Dies reduziert die Komplexität und vereinfacht den Prozess der Anwendungsentwicklung.
- **Niedrige Ressourcennutzung:** SQLite hat geringe Anforderungen an Speicher, Rechenleistung und andere Systemressourcen. Dies macht es ideal für Anwendungen mit begrenzten Ressourcen oder für Prototypen und kleine Anwendungen.
- **Portabilität:** SQLite-Datenbanken sind in einer einzigen Datei gespeichert, was sie leicht zu verschieben und zu verwalten macht. Dadurch können Sie die Datenbank problemlos zwischen verschiedenen Systemen und Entwicklungsumgebungen verschieben.

Im Allgemeinen bietet SQLite eine einfache, effiziente und kostengünstige Möglichkeit zum Speichern und Verwalten von Daten in kleinen und leichten Flask-Anwendungen.

## 2.app.py erwetern
Am besten öffnen wir beide Dateien app.py (Flask01) und app.py(Flask02) und vergleichen die beide.
Die zwei Versionen der Flask-Anwendung unterscheiden sich im Wesentlichen durch die Integration einer SQLite-Datenbank in der zweiten Version. Hier sind die wichtigsten Unterschiede:
## Erste Version
### Einfache Flask-Anwendung mit zwei Routen:

-/ zum Rendern der Index-Seite

-/  calculate zur Verarbeitung einer POST-Anfrage mit dem Radius und dem Rendern der Ergebnisse auf der Index-Seite.

-  Kein Speichern von Daten in einer Datenbank.

## Zweite Version
### Integration einer SQLite-Datenbank zum Speichern von Daten.

Mehrere Funktionen zur Verbindungsherstellung mit der Datenbank und Tabelle calculations.
Mehrere neue Routen:

/ zum Rendern der Index-Seite mit allen gespeicherten Berechnungsergebnissen aus der Datenbank.
        
/ calculate zur Verarbeitung einer POST-Anfrage, Speichern des Berechnungsergebnisses in der Datenbank und Rendern der Ergebnisse auf der Index-Seite.

/ delete/<int:calculation_id> zum Löschen eines bestimmten Eintrags aus der Datenbank.

Im Allgemeinen bietet die zweite Version eine bessere Datenverwaltung durch die Integration einer SQLite-Datenbank. Diese ermöglicht das Speichern, Abfragen und Löschen von Berechnungsergebnissen, was die Funktionalität der Anwendung erweitert und sie für komplexere Anwendungsfälle geeignet macht.
