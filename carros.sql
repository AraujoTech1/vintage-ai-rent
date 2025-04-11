CREATE TABLE IF NOT EXISTS carros (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    ano INT,
    disponivel BOOLEAN
);

INSERT INTO carros (nome, ano, disponivel) VALUES
('Chevrolet Bel Air', 1957, TRUE),
('Mustang Fastback', 1969, FALSE),
('Fusca Clássico', 1974, TRUE);
