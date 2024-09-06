WITH
    contagem_vendas_por_estado AS (
        SELECT 
            estado,
            COUNT(*) AS total
        FROM tbvendas
        WHERE status = 'Concluído'
        GROUP BY estado
    )

SELECT 
    t.estado,
    ROUND(AVG(t.vrunt * t.qtd), 2) AS gastomedio
FROM tbvendas t
JOIN contagem_vendas_por_estado cve
    ON cve.estado = t.estado
WHERE t.status = 'Concluído'
GROUP BY t.estado
ORDER BY gastomedio DESC;
