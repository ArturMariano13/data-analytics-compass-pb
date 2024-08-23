import logging
import boto3
from botocore.exceptions import ClientError
import os
import pandas as pd
import re
import chardet

def detectar_codificacao(arquivo):
    """Detecta a codificação do arquivo usando chardet."""
    with open(arquivo, 'rb') as f:
        resultado = chardet.detect(f.read())
    return resultado['encoding']

def carregar_csv(arquivo, codificacao):
    """Carrega o arquivo CSV com a codificação detectada."""
    return pd.read_csv(arquivo, delimiter=';', encoding=codificacao)

def limpar_espacos(valor):
    """Remove espaços desnecessários do valor."""
    if pd.isna(valor) or not isinstance(valor, str):
        return valor
    valor = valor.strip()
    valor = re.sub(r'\s+', ' ', valor)
    return valor

def formatar_data(data):
    """Formata a data de dd/mm/aaaa para aaaa-mm-dd."""
    if pd.isna(data):
        return data
    try:
        # Primeiro, tenta converter a data para datetime usando o formato esperado
        data_formatada = pd.to_datetime(data, format='%d/%m/%Y', errors='coerce')
        # Verifica se a conversão foi bem-sucedida
        if pd.notna(data_formatada):
            return data_formatada.strftime('%Y-%m-%d')
        else:
            return data  # Retorna o valor original se a conversão falhar
    except ValueError:
        return data  # Retorna o valor original se a conversão falhar

def corrigir_valores(valor):
    """Corrige valores numéricos específicos removendo 'R$', substituindo ',' por '.' e convertendo para float."""
    if pd.isna(valor):
        return valor
    if isinstance(valor, str):
        valor = valor.replace('R$', '').replace('.', '').replace(',', '.').strip()
        return float(valor) if valor else valor
    return valor

def salvar_csv(df, arquivo):
    """Salva o DataFrame em um arquivo CSV com codificação UTF-8."""
    df.to_csv(arquivo, sep=';', index=False, encoding='utf-8')

def upload_arquivo(arquivo, bucket, objeto=None):
    """Faz o upload do arquivo para o bucket S3."""
    if objeto is None:
        objeto = os.path.basename(arquivo)

    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(arquivo, bucket, objeto)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def processar_arquivo(arquivo_original, arquivo_corrigido, bucket_name):
    """Processa o arquivo CSV: detecta codificação, limpa e corrige valores, e faz o upload para o S3."""
    # Detectar codificação e carregar CSV
    codificacao = detectar_codificacao(arquivo_original)
    df = carregar_csv(arquivo_original, codificacao)

    # Aplicar limpeza de espaços e correção de valores numéricos
    for coluna in df.columns:
        df[coluna] = df[coluna].apply(limpar_espacos)

    # Formatar colunas de data
    colunas_de_data = ['Data do Inicio', 'Data da Deflagracao']
    for coluna in colunas_de_data:
        if coluna in df.columns:
            df[coluna] = df[coluna].apply(formatar_data)

    colunas_para_corrigir = [
        "Qtd Prejuizos Causados a Uniao"
    ]
    for coluna in colunas_para_corrigir:
        if coluna in df.columns:
            df[coluna] = df[coluna].apply(corrigir_valores)

    # Salvar o arquivo CSV corrigido
    salvar_csv(df, arquivo_corrigido)
    print(f'Arquivo corrigido com sucesso como {arquivo_corrigido}!')

    # Fazer o upload do arquivo corrigido para o S3
    if upload_arquivo(arquivo_corrigido, bucket_name):
        print(f'Upload do arquivo {arquivo_corrigido} realizado com sucesso!')
    else:
        print(f'Erro ao realizar o upload do arquivo!')

# Configurações
arquivo_original = 'PALAS_OPERACOES_2024_01.csv'
arquivo_corrigido = 'PALAS_OPERACOES_2024_01_corrigido.csv'
bucket_name = 'bucket-operacoes-policiais'

# Executar o processamento do arquivo
processar_arquivo(arquivo_original, arquivo_corrigido, bucket_name)
