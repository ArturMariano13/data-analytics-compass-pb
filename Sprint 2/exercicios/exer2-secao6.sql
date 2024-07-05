SELECT 
	e.codeditora AS "CodEditora",
	e.nome AS "NomeEditora",
	COUNT(*) AS "QuantidadeLivros"
FROM livro l
LEFT JOIN editora e
	ON l.editora = e.codeditora
GROUP BY e.codeditora, e.nome
ORDER BY "QuantidadeLivros" DESC
LIMIT 5;

