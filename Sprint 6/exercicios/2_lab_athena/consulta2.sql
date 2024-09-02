WITH DecadeRanking AS (
  SELECT
    Nome,
    Sexo,
    SUM(Total) AS TotalPorNome,
    CAST(FLOOR(Ano / 10) * 10 AS INT) AS Decada,
    ROW_NUMBER() OVER (PARTITION BY FLOOR(Ano / 10) * 10, Sexo ORDER BY SUM(Total) DESC) AS Posicao
  FROM
    meubanco.nomes
  WHERE
    Ano >= 1950
  GROUP BY
    Nome, Sexo, FLOOR(Ano / 10) * 10
)

SELECT
  Decada,
  ARRAY_JOIN(
    ARRAY_AGG(CASE WHEN Sexo = 'M' AND Posicao <= 3 THEN Nome END ORDER BY TotalPorNome DESC), ', ') AS TopNomesMasculinos,
  ARRAY_JOIN(
    ARRAY_AGG(CASE WHEN Sexo = 'F' AND Posicao <= 3 THEN Nome END ORDER BY TotalPorNome DESC), ', ') AS TopNomesFemininos
FROM
  DecadeRanking
WHERE
  Posicao <= 3
GROUP BY
  Decada
ORDER BY
  Decada;
    