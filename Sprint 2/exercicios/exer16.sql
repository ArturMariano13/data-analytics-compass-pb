WITH 
    vendas_por_estado AS (
        SELECT 
            t.estado,
            t.nmpro,
            SUM(t.qtd) AS total_vendido,
            COUNT(*) AS total_vendas
        FROM tbvendas t
        WHERE t.status = 'Concluído'
        GROUP BY t.estado, t.nmpro
    )

SELECT 
    ve.estado,
    ve.nmpro,
    ROUND(AVG(t.qtd), 4) AS quantidade_media
FROM tbvendas t
JOIN vendas_por_estado ve
    ON ve.estado = t.estado AND ve.nmpro = t.nmpro
WHERE t.status = 'Concluído'
GROUP BY ve.estado, ve.nmpro
ORDER BY ve.estado, ve.nmpro;
