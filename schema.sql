DROP TABLE IF EXISTS chamados;

CREATE TABLE chamados (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  laboratorio TEXT NOT NULL,
  FOREIGN KEY (id) REFERENCES user (id)
);

CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES user (id),
);