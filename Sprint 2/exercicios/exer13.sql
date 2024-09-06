SELECT 
    cdpro,
    nmcanalvendas,
    nmpro,
    SUM(qtd) AS quantidade_vendas
FROM tbvendas
WHERE status = 'Concluído' 
    AND (nmcanalvendas = 'Matriz' OR nmcanalvendas = 'Ecommerce')
GROUP BY cdpro, nmcanalvendas, nmpro
ORDER BY quantidade_vendas
LIMIT 10;
