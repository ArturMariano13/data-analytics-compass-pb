WITH
	total_gasto AS (
		SELECT
			cdcli,
			nmcli,
			SUM(vrunt * qtd) AS valor_gasto
		FROM tbvendas tv
		WHERE status = 'Concluído'
		GROUP BY cdcli, nmcli
	)

SELECT 
	cdcli,
	nmcli,
	MAX(valor_gasto) AS gasto
FROM total_gasto;