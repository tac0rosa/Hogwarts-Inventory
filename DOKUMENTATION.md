# Dokumentation — Hogwarts Inventory

Sarah Prante, Rocio Sainz
Agile Webanwendung mit Python
WiSe 2025/2026
https://github.com/tac0rosa/Hogwarts-Inventory

> Dieses Dokument wird im Laufe der Entwicklung nach und nach vervollständigt (siehe Abschnitt "Documentation" in `TASKS.md`), nicht alles auf einmal am Ende.

## 1. Motivation und Anforderungen

### 1.1 Projektidee

Die Idee zu Hogwarts Inventory ist aus unserer gemeinsamen Begeisterung für Harry Potter entstanden. Anstatt eine thematisch neutrale, "langweilige" Inventarverwaltung zu bauen, wollten wir ein Thema wählen, das uns beide während der Entwicklung motiviert und mit dessen Figuren, Orten und Regeln wir uns ohnehin gut auskennen. Im Kern ist Hogwarts Inventory eine klassische CRUD-Anwendung zur Verwaltung von Datensätzen mit Beziehungen untereinander — nur eben verpackt in die Welt von Hogwarts, der Schule für Hexerei und Zauberei, statt in ein generisches Firmen- oder Lagerbeispiel.

### 1.2 Ideensammlung

Wir haben uns auf vier zusammenhängende Entitäten festgelegt: Häuser, Professor\*innen, Schüler\*innen und Gegenstände. Ein Haus hat Professor\*innen und Schüler\*innen, Schüler\*innen haben optional eine\*n Berater\*in, und Gegenstände gehören zu einem Haus und optional einer\*einem Schüler\*in. Damit ergibt sich ein kleines, aber vollständiges Beziehungsgeflecht, an dem sich CRUD-Operationen über mehrere verknüpfte Modelle hinweg sinnvoll zeigen lassen.

### 1.3 Anforderungen an das Projekt

Hogwarts Inventory soll die vollständige Verwaltung (Anlegen, Anzeigen, Bearbeiten, Löschen) von vier Datentypen ermöglichen:

- **Houses**: Name, Gründer\*in, Gemeinschaftsraum, Hauspunkte.
- **Professors**: Name, unterrichtetes Fach, Büro, optional das Haus, dessen Hauslehrer\*in sie/er ist.
- **Students**: Name, Jahrgangsstufe, zugehöriges Haus (Pflicht), optional ein\*e Professor\*in als Berater\*in.
- **Items**: Name, Kategorie, Menge, Beschreibung, verpflichtend zugehöriges Haus, optional eine\*n Besitzer\*in (Student).

Dabei soll jede Entität sowohl über das automatisch generierte Django-Admin-Interface als auch über eigene, selbst gestaltete Views und Templates verwaltbar sein — Nutzer\*innen der Anwendung sollen also nicht zwingend auf das Admin-Interface angewiesen sein. Löschregeln sollen die Datenintegrität sicherstellen (z. B. werden Gegenstände eines Hauses mitgelöscht, wenn das Haus gelöscht wird). Die Anwendung soll lokal mit einer SQLite-Datenbank lauffähig sein, ohne zusätzliche Infrastruktur.

### 1.4 Recherchen und bestehende Lösungen

Eine direkte Konkurrenz zu einer Verwaltungsanwendung für eine fiktive Zauberschule gibt es naturgemäß nicht — hier lohnt sich die Recherche eher auf Ebene der beiden realen Konzepte, die hinter Hogwarts Inventory stecken: Schulverwaltungssoftware und Inventar-/Asset-Tracking.

Im Bereich Schulverwaltung mit Django sind wir unter anderem auf [Django-SIS](https://github.com/burke-software/schooldriver) gestoßen, ein quelloffenes School Information System, das bewusst stark auf das Django-Admin-Interface setzt, um Schüler\*innen-, Eltern- und Lehrer\*innendaten zu verwalten. Das deckt sich mit unserem eigenen Ansatz, admin.py von Anfang an vollständig zu pflegen und die eigenen CRUD-Views quasi als "hübschere" Oberfläche über denselben Daten zu bauen. Daneben gibt es diverse kleinere [Django School Management Systeme](https://github.com/topics/school-management-system) auf GitHub, die im Kern dieselben Grundoperationen (Schüler\*innen, Lehrkräfte, Klassen/Kurse verwalten) abdecken wie unsere Students/Professors-Verwaltung.

Für den Items-Teil ist die naheliegende reale Kategorie Asset- bzw. Inventarverwaltungssoftware wie [Sortly](https://www.sortly.com/) oder [Asset Panda](https://www.assetpanda.com/), die Gegenstände mit Menge, Kategorie und Zuordnung zu einem Ort oder einer Person verwalten — strukturell sehr ähnlich zu unserem Item-Modell (Menge, Kategorie, zugehöriges Haus, optionale\*r Besitzer\*in), nur eben für reale statt magische Gegenstände.

Quellen zu diesem Abschnitt sind auch in Abschnitt 6 (Quellen) aufgeführt.

## 2. Planung und Design

_TODO: Aufgabenverteilung und Teamorganisation, gewähltes Framework/Entwicklungsumgebung/Tools, Diagramm der Datenbankstruktur._

## 3. Entwicklung

_TODO: Beschreibung der Funktionalitäten (mit Screenshots) und technische Herausforderungen (mit Codeausschnitten). Ein Abschnitt pro CRUD-Bereich (Houses, Professors, Students, Items)._

### Houses

### Professors

### Students

### Items

## 4. Inbetriebnahme

_TODO: Schritte zur lokalen Inbetriebnahme des Projekts (siehe auch `README.md`)._

## 5. Fazit

_TODO: welche ursprünglichen Anforderungen umgesetzt wurden, persönliche Einschätzung, mögliche Erweiterungen oder zukünftige Verbesserungen._

## 6. Quellen

_TODO: URLs und Referenzen zu verwendeten Bibliotheken oder Code von Dritten._
