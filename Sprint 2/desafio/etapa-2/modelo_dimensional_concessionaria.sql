-- MODELO DIMENSIONAL

-- dimensões
CREATE VIEW dim_Cliente AS
SELECT
	idCliente AS CodigoCliente,
	nomeCliente AS NomeCliente,
	cidadeCliente AS CidadeCliente,
	estadoCliente AS EstadoCliente,
    paisCliente AS PaisCliente
FROM clientes;


CREATE VIEW dim_Vendedor AS
SELECT
	idVendedor AS CodigoVendedor,
	nomeVendedor AS NomeVendedor,
	sexoVendedor AS SexoVendedor,
	estadoVendedor AS EstadoVendedor
FROM vendedores;


CREATE VIEW dim_Carro AS
SELECT
	c.idCarro AS CodigoCarro,
	c.kmCarro AS QuilometragemCarro,
	c.chassiCarro AS ChassiCarro,
    c.marcaCarro AS MarcaCarro,
    c.modeloCarro AS ModeloCarro,
    c.anoCarro AS AnoCarro,
    co.tipoCombustivel AS TipoCombustivel
FROM carros c
JOIN combustiveis co ON c.idCombustivel = co.idCombustivel;


CREATE VIEW dim_DataLocacao AS
SELECT 
    l.idLocacao AS CodigoLocacao,
    l.dataLocacao AS DataLocacaoCompleta,
    l.horaLocacao AS HoraLocacao,
    SUBSTR(l.dataLocacao, 1, 4) AS AnoLocacao,
    SUBSTR(l.dataLocacao, 5, 2) AS MesLocacao,
    SUBSTR(l.dataLocacao, 7, 2) AS DiaLocacao
FROM locacoes l;

CREATE VIEW dim_DataEntrega AS
SELECT 
	l.idLocacao AS CodigoLocacao,
    l.dataEntrega AS DataEntregaCompleta,
    l.horaEntrega AS HoraEntrega,
    SUBSTR(l.dataEntrega, 1, 4) AS AnoEntrega,
    SUBSTR(l.dataEntrega, 5, 2) AS MesEntrega,
    SUBSTR(l.dataEntrega, 7, 2) AS DiaEntrega
FROM locacoes l;

-- FATO: locação
CREATE VIEW fato_Locacoes AS
SELECT
	l.idLocacao AS CodigoLocacao,
	l.idCliente AS CodigoCliente,
	l.idCarro AS CodigoCarro,
	l.idVendedor AS CodigoVendedor,
	l.qtdDiaria AS QuantidadeDiarias,
	l.vlrDiaria AS ValorDiaria,
	l.dataLocacao AS DataLocacao,
	l.dataEntrega AS DataEntrega
FROM locacoes l;

SELECT * FROM dim_Cliente;
SELECT * FROM dim_Vendedor; 
SELECT * FROM dim_DataLocacao;
SELECT * FROM dim_DataEntrega;
SELECT * FROM dim_Carro; 
SELECT * FROM fato_Locacoes; 
