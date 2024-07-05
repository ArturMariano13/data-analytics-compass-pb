WITH 
    valores_venda AS (
        SELECT
            cdvdd AS codigo_vendedor,
            SUM(vrunt * qtd) AS valor_venda
        FROM tbvendas
        WHERE status = 'Concluído'
        GROUP BY cdvdd
    ),
    vendedor_com_menor_venda AS (
        SELECT 
            codigo_vendedor,
            valor_venda
        FROM valores_venda
        WHERE valor_venda = (
            SELECT MIN(valor_venda)
            FROM valores_venda
            WHERE valor_venda > 0
        )
        LIMIT 1
    )
SELECT 
    d.cddep,
    d.nmdep,
    d.dtnasc,
    vcmv.valor_venda AS valor_total_vendas
FROM tbdependente d
JOIN vendedor_com_menor_venda vcmv
    ON d.cdvdd = vcmv.codigo_vendedor
ORDER BY d.cddep;
