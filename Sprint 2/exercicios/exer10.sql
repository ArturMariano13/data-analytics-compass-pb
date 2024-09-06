WITH
    total_vendas AS (
        SELECT 
            cdvdd AS codigo_vendedor,
            SUM(vrunt * qtd) AS total
        FROM tbvendas
        WHERE status = 'Concluído'
        GROUP BY cdvdd
    )

SELECT 
    t.nmvdd AS vendedor,
    ROUND(total, 2) AS valor_total_vendas,
    ROUND(total * t.perccomissao / 100, 2) AS comissao
FROM total_vendas tv
JOIN tbvendedor t 
    ON t.cdvdd = tv.codigo_vendedor
ORDER BY comissao DESC;