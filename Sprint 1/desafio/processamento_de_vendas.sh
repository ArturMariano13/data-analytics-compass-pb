#!/bin/bash

ECOMMERCE_DIR="/home/artur/data-analytics-compass-pb/Sprint 1/desafio/ecommerce"
VENDAS_DIR="/home/artur/data-analytics-compass-pb/Sprint 1/desafio/vendas"
BACKUP_DIR="${VENDAS_DIR}/backup"
FILE_NAME="dados_de_vendas.csv"
CURRENT_DATE=$(date +"%Y%m%d")
CURRENT_DATETIME=$(date +"%Y/%m/%d %H:%M")
BACKUP_FILE="dados-${CURRENT_DATE}.csv"
FINAL_BACKUP_FILE="backup-dados-${CURRENT_DATE}.csv"
REPORT_FILE="relatorio.txt"
REPORT_FILE_DIF="${CURRENT_DATE}-relatorio.txt"

mkdir -p "${VENDAS_DIR}"
cp "${ECOMMERCE_DIR}/${FILE_NAME}" "${VENDAS_DIR}/"

mkdir -p "${BACKUP_DIR}"
cp "${VENDAS_DIR}/${FILE_NAME}" "${BACKUP_DIR}/${BACKUP_FILE}"

mv "${BACKUP_DIR}/${BACKUP_FILE}" "${BACKUP_DIR}/${FINAL_BACKUP_FILE}"

FIRST_DATE=$(head -2 "${BACKUP_DIR}/${FINAL_BACKUP_FILE}" | tail -1 | cut -d, -f5)
LAST_DATE=$(tail -1 "${BACKUP_DIR}/${FINAL_BACKUP_FILE}" | cut -d, -f5)
TOTAL_ITEMS=$(tail -n +2 "${BACKUP_DIR}/${FINAL_BACKUP_FILE}" | cut -d, -f2 | sort | uniq | wc -l)

echo "Data do sistema operacional: ${CURRENT_DATETIME}" > "${BACKUP_DIR}/${REPORT_FILE}"
echo "Data do primeiro registro de venda: ${FIRST_DATE}" >> "${BACKUP_DIR}/${REPORT_FILE}"
echo "Data do último registro de venda: ${LAST_DATE}" >> "${BACKUP_DIR}/${REPORT_FILE}"
echo "Quantidade total de itens diferentes vendidos: ${TOTAL_ITEMS}" >> "${BACKUP_DIR}/${REPORT_FILE}"
echo "" >> "${BACKUP_DIR}/${REPORT_FILE}"
echo "Primeiras 10 linhas do arquivo ${FINAL_BACKUP_FILE}:" >> "${BACKUP_DIR}/${REPORT_FILE}"
head -10 "${BACKUP_DIR}/${FINAL_BACKUP_FILE}" >> "${BACKUP_DIR}/${REPORT_FILE}"

zip "${BACKUP_DIR}/${FINAL_BACKUP_FILE}.zip" "${BACKUP_DIR}/${FINAL_BACKUP_FILE}"

rm "${BACKUP_DIR}/${FINAL_BACKUP_FILE}"
rm "${VENDAS_DIR}/${FILE_NAME}"

mv "${BACKUP_DIR}/${REPORT_FILE}" "${BACKUP_DIR}/${REPORT_FILE_DIF}"

echo "Relatório de processamento de vendas gerado com sucesso!"

