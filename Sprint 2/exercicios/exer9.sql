WITH
    mais_vendido AS (
        SELECT
            cdpro,
            nmpro,
            COUNT(*) AS contagem
        FROM tbvendas 
        WHERE status = 'Concluído' 
          AND dtven BETWEEN '2014-02-03' AND '2018-02-02'
        GROUP BY cdpro, nmpro
    )
    
SELECT 
    mv.cdpro,
    mv.nmpro
FROM mais_vendido mv
WHERE mv.contagem = (
    SELECT 
        MAX(contagem)
    FROM mais_vendido
)
ORDER BY mv.cdpro, mv.nmpro;
