WITH
    editoras_fora_sul AS (
        SELECT
            ed.codeditora,
            ed.endereco,
            e.estado
        FROM editora ed
        LEFT JOIN endereco e
            ON ed.endereco = e.codendereco
        WHERE e.estado <> 'RIO GRANDE DO SUL'
          AND e.estado <> 'PARANÁ'
          AND e.estado <> 'SANTA CATARINA'
    ),
    autores AS (
        SELECT 
            DISTINCT l.autor
        FROM livro l
        LEFT JOIN editoras_fora_sul efs
            ON efs.codeditora = l.editora
        WHERE efs.codeditora IS NOT NULL
    )
SELECT 
    a.nome
FROM autores au
JOIN autor a
    ON au.autor = a.codautor
ORDER BY a.nome;
