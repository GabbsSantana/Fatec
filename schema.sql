DROP TABLE IF EXISTS chamados;
CREATE TABLE chamados(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  micro INTEGER NOT NULL,
  laboratorio TEXT NOT NULL,
  CONSTRAINT fk_alunos FOREIGN KEY (alunos_id) REFERENCES alunos(alunos_id)
);
DROP TABLE IF EXISTS layout;
CREATE TABLE layout(
  laboratorio_id INTEGER PRIMARY KEY AUTOINCREMENT,
  laboratorio_nome TEXT NOT NULL,
  layout_nome TEXT NOT NULL
);
DROP TABLE IF EXISTS alunos;
CREATE TABLE alunos (
  aluno_id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  email TEXT NOT NULL
);