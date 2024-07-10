-- MODELO DIMENSIONAL

-- dimensões
CREATE VIEW dim_cliente AS
SELECT
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
    paisCliente
FROM clientes;

CREATE VIEW dim_vendedor AS
SELECT
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM vendedores;

CREATE VIEW dim_combustivel AS
SELECT
	idCombustivel,
	tipoCombustivel
FROM combustiveis;

CREATE VIEW dim_carro AS
SELECT
	c.idCarro,
	c.kmCarro,
	c.chassiCarro,
    c.marcaCarro,
    c.modeloCarro,
    c.anoCarro,
    c.idCombustivel,
    co.tipoCombustivel
FROM carros c
JOIN combustiveis co ON c.idCombustivel = co.idCombustivel;

-- FATOS
CREATE VIEW fato_locacoes AS
SELECT
	l.idLocacao,
	l.idCliente,
	l.idCarro,
	l.idVendedor,
	l.dataLocacao,
	l.horaLocacao,
	l.qtdDiaria,
	l.vlrDiaria,
	l.dataEntrega,
	l.horaEntrega,
	c.nomeCliente,
	c.cidadeCliente,
	c.estadoCliente,
	c.paisCliente,
	ca.kmCarro,
	ca.chassiCarro,
	ca.marcaCarro,
	ca.modeloCarro,
	ca.anoCarro,
	ca.idCombustivel,
	co.tipoCombustivel,
	v.nomeVendedor,
	v.sexoVendedor,
	v.estadoVendedor
FROM locacoes l
JOIN clientes c ON l.idCliente = c.idCliente
JOIN carros ca ON l.idCarro = ca.idCarro
JOIN combustiveis co ON ca.idCombustivel = co.idCombustivel
JOIN vendedores v ON l.idVendedor = v.idVendedor;

SELECT * FROM dim_cliente;
SELECT * FROM dim_vendedor; 
SELECT * FROM dim_combustivel; 
SELECT * FROM dim_carro; 
SELECT * FROM fato_locacoes; 


