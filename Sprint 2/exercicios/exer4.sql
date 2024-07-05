SELECT 
    a.nome,
    a.codautor,
    a.nascimento,
    COUNT(l.cod) AS quantidade
FROM autor AS a
LEFT JOIN livro AS l
    ON l.autor = a.codautor
GROUP BY a.codautor, a.nome, a.nascimento
ORDER BY a.nome;