CREATE TABLE clientes(
	idCliente INTEGER PRIMARY KEY NOT NULL,
	nomeCliente VARCHAR(100) NOT NULL,
	cidadeCliente VARCHAR(40) NOT NULL,
	estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

CREATE TABLE vendedores (
	idVendedor INTEGER PRIMARY KEY NOT NULL,
	nomeVendedor VARCHAR(15) NOT NULL,
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR(40)
);

CREATE TABLE combustiveis (
	idCombustivel INTEGER PRIMARY KEY NOT NULL,
	tipoCombustivel VARCHAR(20)
);

CREATE TABLE carros (
	idCarro INTEGER PRIMARY KEY NOT NULL,
	kmCarro INTEGER NOT NULL,
	chassiCarro VARCHAR(50) NOT NULL,
    marcaCarro VARCHAR(80) NOT NULL,
    modeloCarro VARCHAR(60) NOT NULL,
    anoCarro INTEGER NOT NULL,
    idCombustivel INTEGER NOT NULL,
    FOREIGN KEY (idCombustivel) REFERENCES combustiveis(idCombustivel)
);

CREATE TABLE locacoes (
	idLocacao INTEGER PRIMARY KEY NOT NULL,
	idCliente INTEGER NOT NULL,
	idCarro INTEGER NOT NULL,
	idVendedor INTEGER NOT NULL,
	dataLocacao DATETIME NOT NULL,
	horaLocacao TIME NOT NULL,
	qtdDiaria INTEGER NOT NULL,
	vlrDiaria DECIMAL(18,2) NOT NULL,
	dataEntrega DATE,
	horaEntrega TIME,
	FOREIGN KEY (idCliente) REFERENCES clientes(idCliente),
	FOREIGN KEY (idCarro) REFERENCES carros(idCarro),
	FOREIGN KEY (idVendedor) REFERENCES vendedores(idVendedor)
);

-- INSERÇÕES

-- inserção na tabela clientes
INSERT INTO clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente 
FROM tb_locacao;

-- inserção na tabela vendedores
INSERT INTO vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor 
FROM tb_locacao;

-- inserção na tabela combustiveis
INSERT INTO combustiveis (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;

-- inserção na tabela carros
INSERT INTO carros (idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
WITH LatestKm AS (
    SELECT 
        classicarro,
        MAX(kmcarro) AS max_kmcarro
    FROM tb_locacao
    GROUP BY classiCarro
)
SELECT 
    t1.idcarro, t1.kmcarro, 
    t1.classicarro, t1.marcacarro, t1.modelocarro, 
    t1.anocarro, t1.idcombustivel
FROM tb_locacao t1
JOIN LatestKm t2
ON t1.classicarro = t2.classicarro AND t1.kmcarro = t2.max_kmcarro;

-- inserção na tabela locacoes
INSERT INTO locacoes (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao;
