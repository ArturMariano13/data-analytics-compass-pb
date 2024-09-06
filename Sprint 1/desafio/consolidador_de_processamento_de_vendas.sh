#!/bin/bash

BACKUP_DIR="/home/artur/data-analytics-compass-pb/Sprint 1/desafio/vendas/backup"
FINAL_REPORT="relatorio_final.txt"

rm -f "${BACKUP_DIR}/${FINAL_REPORT}"

echo "Relatório Consolidado de Vendas" > "${BACKUP_DIR}/${FINAL_REPORT}"
echo "===========================================================================================" >> "${BACKUP_DIR}/${FINAL_REPORT}"
echo "" >> "${BACKUP_DIR}/${FINAL_REPORT}"

COUNTER=1

for REPORT in "${BACKUP_DIR}"/*-relatorio.txt; do
	echo "Relatório ${COUNTER}" >> "${BACKUP_DIR}/${FINAL_REPORT}"
	echo "------------------------------------------------------" >> "${BACKUP_DIR}/${FINAL_REPORT}"

	cat "${REPORT}" >> "${BACKUP_DIR}/${FINAL_REPORT}"
	echo "" >> "${BACKUP_DIR}/${FINAL_REPORT}"
	echo "" >> "${BACKUP_DIR}/${FINAL_REPORT}"

	COUNTER=$((COUNTER+1))
done




