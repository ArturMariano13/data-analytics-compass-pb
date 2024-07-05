WITH qtd AS (
    SELECT
        l.autor,
        a.nome,
        COUNT(l.autor) AS quantidade
    FROM livro l
    LEFT JOIN autor a
        ON a.codautor = l.autor
    GROUP BY l.autor, a.nome
)

SELECT 
    q.autor AS codautor,
    q.nome,
    MAX(q.quantidade) AS quantidade_publicacoes
FROM qtd q
ORDER BY q.quantidade DESC;