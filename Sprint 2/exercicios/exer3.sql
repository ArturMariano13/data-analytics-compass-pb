WITH
	cidade_estado AS (
		SELECT 
			ender.estado AS estado,
			ender.cidade AS cidade,
			ed.nome AS nome,
			ed.codeditora AS codeditora
		FROM endereco AS ender
		LEFT JOIN editora AS ed
			ON ed.endereco = ender.codendereco
	),
	
	editora_livro_count AS (
        SELECT
            l.editora AS codeditora,
            COUNT(*) AS quantidade
        FROM livro AS l
        GROUP BY l.editora
    )
	
SELECT 
    elc.quantidade,
    ce.nome,
    ce.estado,
    ce.cidade
FROM editora_livro_count AS elc
JOIN cidade_estado AS ce
    ON elc.codeditora = ce.codeditora
ORDER BY elc.quantidade DESC
LIMIT 5;