SELECT 
    MAX(DATE_DIFF(month, TO_TIMESTAMP("Data do Inicio"), TO_TIMESTAMP("Data da Deflagracao"))) AS "Maior diferença deflagração e início (meses)",
    SUM(CASE WHEN LOWER("Tipo de Operacao") = 'operacao especial' THEN 1 ELSE 0 END) AS "Total Operações Especiais",
    COUNT(*) AS "Total de Registros"
FROM 
    S3Object
WHERE 
    "Atuacao em Territorio Indigena" = 'Nao' 
    AND (CAST("Qtd Prisao em Flagrante" AS INTEGER) > 0 OR CAST("Qtd Mandado de Busca e Apreesao" AS INTEGER) > 0);