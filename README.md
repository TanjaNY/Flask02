
# Richtige Datenbank für die Anwendung auswählen

# Flask02
Das ist die zweite Flask-Lektion, die erste Lektion findest du hier:https://github.com/TanjaNY/Flask


## Wenn Du Flask01 nicht mitgemacht hast..
### a. GitHub-Repository klonen:

- Öffne die Kommandozeile (cmd) auf deinem Windows-Computer.
- Navigiere zu dem Verzeichnis, in das du die Anwendung klonen möchtest.
- Verwende den folgenden Befehl, um das Repository von GitHub zu klonen:

```bash
git git clone https://github.com/TanjaNY/Flask02.git
```

### b. Flask-Umgebung erstellen:

- Öffne die Conda-Befehlszeile.
- Füge dein Anaconda-Verzeichnis zu den Umgebungsvariablen hinzu [Anleitung](https://michster.de/wie-setze-ich-die-path-umgebungsvariablen-unter-windows-10/).
- Verwende den folgenden Befehl, um eine neue Conda-Umgebung zu erstellen:

```bash
conda create --name flask_env 
```

- Aktiviere die erstellte Umgebung mit dem Befehl:

```bash
conda activate flask_env
```
- Anaconda ist nicht zwingend erforderlich, um eine Flask-App zu entwickeln. Du benötigst Anaconda, wenn du Data Science meistern möchtest. Im Fall, dass du dich gegen Anaconda entscheidest, werden die Befehle etwas anders aussehen.


```bash
python -m venv flask_env 
```


```bash
flask_env\Scripts\activate
```

## c. Flask und Werkzeug installieren:

Flask und Werkzeug sind zwei Python-Pakete, die für die Webentwicklung verwendet werden.
Flask ist ein leichtgewichtiges Webframework für Python, das die Entwicklung von Webanwendungen und APIs erleichtert. Es bietet eine einfache und intuitive API, die Entwicklern ermöglicht, einfache, aber leistungsfähige Web-Apps schnell und effizient zu entwickeln.
Werkzeug ist eine Python-Bibliothek, die eine Sammlung von Werkzeugen und Bibliotheken für die Entwicklung von Webanwendungen bereitstellt. Es bietet Funktionen wie HTTP-Verwaltung, Anwendungsobjekte und Debugging-Funktionen, die in Flask und anderen Python-Webframeworks verwendet werden können.
Werkzeug stellt somit eine wichtige Infrastruktur für die Entwicklung von Web-Apps und APIs mit Python dar.


- In der aktivierten Conda-Umgebung führe die folgenden Befehle aus, um Flask und Werkzeug zu installieren:

```bash
pip install flask 
pip install Werkzeug 
```
## c. Warum brauchen wir eine Python-Umgebung?:

### Hauptgründe für separate Umgebungen
Die Hauptmotivation für separate Entwicklungsumgebungen liegt in der Isolierung von Projektabhängigkeiten. Jedes Softwareprojekt hat unterschiedliche Anforderungen an Bibliotheken und deren Versionen. Wenn Pakete global installiert werden, entstehen schnell Konflikte zwischen verschiedenen Projekten.
Vorteile von isolierten Umgebungen

### Versionskompatibilität
Unterschiedliche Projekte benötigen oft verschiedene Versionen derselben Bibliothek. Eine isolierte Umgebung ermöglicht es, genau die benötigten Versionen zu installieren, ohne andere Projekte zu beeinträchtigen.
Sauberkeit und Übersichtlichkeit
Virtuelle Umgebungen halten das globale Python-System sauber. Alle projektspezifischen Abhängigkeiten werden separat verwaltet, was die Übersicht und Wartbarkeit erhöht.
Reproduzierbarkeit
Durch die Dokumentation der Abhängigkeiten in einer Datei wie requirements.txt kann das Projekt exakt reproduziert werden - auf jedem Computer und von jedem Entwickler.

### Installationsmethoden
Es gibt zwei Hauptmethoden zur Abhängigkeitsverwaltung:

Direkte Installation aller Pakete in der Umgebung
Verwendung einer requirements.txt-Datei zur Paketverwaltung

Bei kleineren Projekten wie unserem, mit wenigen Abhängigkeiten, ist die direkte Installation oft am einfachsten. Die requirements.txt bietet jedoch den Vorteil der besseren Dokumentation und Versionskontrolle.

Eine gut gepflegte Python-Umgebung ist der Schlüssel zu stabilen, wartbaren und portablen Softwareprojekten. Sie verhindert Konflikte, erleichtert die Zusammenarbeit und sorgt für Konsistenz über verschiedene Entwicklungssysteme hinweg.

## 1. Hinzufügen einer Datenbank zur Anwendung
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
In unserer Anwendung haben wir uns für die Verwendung von SQLite entschieden und benötigen daher keinen Datenbankcontainer. Allerdings müsste bei der Verwendung anderer Datenbanken wie MySQL oder PostgreSQL ein Datenbankcontainer eingerichtet werden. In diesem Fall müsste die Datei docker-compose.yaml bzw. compose.yaml angepasst werden, um den Datenbankcontainer hinzuzufügen.

## 2. Integration von SQLite
Vorbereitungen:

Wir stellen sicher , dass Sie die sqlite3-Bibliothek installiert haben:

```bash
pip install sqlite3
```

### 3.Aktualisierung der app.py:

Die Datei app.py enthält den Hauptcode unserer Anwendung. Wir aktualisieren sie nun für die SQLite-Integration.

### Und so können wir.. 

die DSQLite-Bibliothek importieren:


```bash
import sqlite3
```
Eine Datenbank-Verbindung herstellen:

```bash
conn = sqlite3.connect('flask_app.db')
c = conn.cursor()
```
Tabellenkalkulationen erstellen:

```bash
c.execute('''CREATE TABLE IF NOT EXISTS calculations (
                radius REAL,
                area REAL
            )''')
```
Berechnungsergebnissen speichern:


```bash
def save_calculation(radius, area):
    c.execute('INSERT INTO calculations (radius, area) VALUES (?, ?)', (radius, area))
    conn.commit()
```
 gespeicherte Ergebnisse abrufen:


```bash
def get_calculations():
    c.execute('SELECT * FROM calculations')
    return c.fetchall()
```

Einträge löschen:


```bash
def delete_calculation(calculation_id):
    c.execute('DELETE FROM calculations WHERE id = ?', (calculation_id,))
    conn.commit()
```
### Anpassen der Routen:

Wir aktualisieren  die Routen "/" und "/calculate" für die neuen Funktionen.

Die Datei index.html enthält die HTML-Vorlage. Wir aktualisieren sie, um die gespeicherten Ergebnisse anzuzeigen und das Löschen einzelner Einträge zu ermöglichen.

### Änderungen in index.html:

Im Abschnitt für gespeicherte Berechnungen werden HTML, Jinja2-Template-Syntax und Bootstrap-CSS-Klassen angesetzt. Die HTML-Struktur wird verwendet, um eine Tabelle mit den Spalten "Radius", "Fläche" und "Aktion" zu definieren. Die Bootstrap-Klasse table wird verwendet, um die Tabelle stilvoll und für mobile Geräte ansprechend zu gestalten.
Jinja2-Syntax wird verwendet, um die Daten aus der Datenbank zu rendern und dynamische Inhalte innerhalb der HTML-Seite zu erstellen. Das {% for %}-Schleifenelement iteriert über alle berechneten Werte in der Variablen calculations und fügt eine neue Zeile für jeden berechneten Radius und die zugehörige Fläche hinzu. Zudem gibt es einen Link zum Löschen der berechneten Werte aus der Datenbank.
Die Kombination von HTML, CSS, JavaScript und Template-Engines wie Jinja2 ermöglicht es, komplexe und benutzerfreundliche Webapplikationen zu erstellen, indem sie Präsentation, Interaktion und Inhaltsgenerierung effizient und effektiv kombinieren.

HTML
```bash
{% if calculations %}
    <h2>Gespeicherte Berechnungen</h2>
    <table class="table">
        <thead>
            <tr>
                <th>Radius</th>
                <th>Fläche</th>
                <th>Aktion</th>
            </tr>
        </thead>
        <tbody>
            {% for calculation in calculations %}
                <tr>
                    <td>{{ calculation.radius }}</td>
                    <td>{{ calculation.area }}</td>
                    <td>
                        <a href="/delete/{{ calculation.id }}">Löschen</a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endif %}
```


## 4.Vergleich von Code-Versionen: app.py (Flask01) vs. app.py (Flask02)


Öffnen wir die beiden Dateien app.py (Flask01) und app.py (Flask02) und vergleichen  sie. Die Hauptunterschiede zwischen den beiden Versionen der Flask-Anwendung liegen in der Integration einer SQLite-Datenbank in die Version 2.

### Version 1:

Einfache Flask-Anwendung mit zwei Routen:
/: Rendert die Index-Seite
/calculate: Verarbeitet eine POST-Anfrage mit dem Radius, berechnet das Ergebnis und rendert es auf der Index-Seite
Speichert keine Daten in einer Datenbank
<p>&nbsp;</p>

### Version 2:
<p>&nbsp;</p>
Integriert eine SQLite-Datenbank zur Datenspeicherung:
Bietet Funktionen zur Verbindungsherstellung mit der Datenbank und der Tabelle calculations
<p>&nbsp;</p>
Neue Routen:
<p>&nbsp;</p>
"/: " Rendert die Index-Seite mit allen gespeicherten Berechnungsergebnissen aus der Datenbank
<p>&nbsp;</p>
"/calculate " :  Verarbeitet eine POST-Anfrage, speichert das Ergebnis in der Datenbank und rendert es auf der Index-Seite.
<p>&nbsp;</p>
"/delete/<int:calculation_id> ":  Löscht einen bestimmten Eintrag aus der Datenbank.
<p>&nbsp;</p>

Die zweite Version bietet durch die Integration einer SQLite-Datenbank eine deutlich verbesserte Datenverwaltung. Dies ermöglicht die Speicherung, Abfrage und Löschung von Berechnungsergebnissen, was die Funktionalität der Anwendung erweitert und sie für komplexere Anwendungsfälle besser geeignet macht.

## 5. Die Anwendung starten.

- Navigiere zum Verzeichnis der geklonten Flask-Anwendung.
- Wenn du Flask01 nicht mitgemacht hast, lese Flask01/3. Flask-Umgebung erstellen.
- Aktiviere die Umgebung mit dem Befehl:

```bash
flask_env\Scripts\activate
```
- Stare  die Flask-Anwendung
```bash
flask run
```

Wir öffnen unser Webbrowser und geben die Adresse [http://127.0.0.1:5000](http://127.0.0.1:5000) in die Adressleiste ein, um unsere Anwendung zu sehen.

<p>&nbsp;</p>

<p><img src="https://github.com/TanjaNY/Flask/blob/main/pics/Flask02.png" alt="Flask App" &nbsp;&nbsp;&nbsp;&nbsp /></p>

<p>&nbsp;</p>

### Wir können beobachten wie veränderte sich unsere Anwendung.

<p>&nbsp;</p>

<p><img src="https://github.com/TanjaNY/Flask/blob/main/pics/flask01.png" widht="100" height="200" alt="Flask App" &nbsp;&nbsp;&nbsp;&nbsp /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>



<p><img src="https://github.com/TanjaNY/Flask/blob/main/pics/Flask003.png" widht="300" height="500" alt="Flask App" &nbsp;&nbsp;&nbsp;&nbsp /></p>


<p>&nbsp;</p>

### Wir können nochmals mit dem Containern probieren.Alles wird wie hier:

[Flask01](https://github.com/TanjaNY/Flask))

### gemacht!



