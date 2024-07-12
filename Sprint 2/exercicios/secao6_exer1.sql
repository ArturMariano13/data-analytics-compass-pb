WITH
	autores AS (
		SELECT
			codautor,
			nome
		FROM autor
	),
	
	editoras AS (
		SELECT
			codeditora,
			nome
		FROM editora
	)
	

SELECT 
	cod AS "CodLivro",
	titulo AS "Titulo",
	autor AS "CodAutor",
	a.nome AS "NomeAutor",
	valor AS "Valor",
	editora AS "CodEditora",
	e.nome AS "NomeEditora"
FROM livro l
LEFT JOIN autores a
	ON l.autor = a.codautor
LEFT JOIN editora e
	ON l.editora = e.codeditora
ORDER BY valor DESC
LIMIT 10;