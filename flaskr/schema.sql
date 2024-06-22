DROP TABLE IF EXISTS aufgabe;

CREATE TABLE aufgabe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  titel TEXT NOT NULL,
  beginn DATE NOT NULL,
  enddatum DATE NOT NULL,
  fortschritt INT NOT NULL,
  prioritaet TEXT NOT NULL
);