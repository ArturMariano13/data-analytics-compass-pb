WITH
    total_vendas AS (
        SELECT 
            cdvdd AS codigo_vendedor,
            COUNT(*) AS num_vendas
        FROM tbvendas
        WHERE status = 'Concluído'
        GROUP BY cdvdd
    ),
    max_vendas AS (
        SELECT 
            MAX(num_vendas) AS max_vendas
        FROM total_vendas
    )
    
SELECT 
    tv.codigo_vendedor AS cdvdd,
    t.nmvdd AS nmvdd
FROM total_vendas tv
JOIN max_vendas mv
    ON tv.num_vendas = mv.max_vendas
JOIN tbvendedor t
    ON tv.codigo_vendedor = t.cdvdd
ORDER BY t.nmvdd;