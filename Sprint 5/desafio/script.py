import boto3
import logging
from botocore.exceptions import ClientError
import os
import pandas as pd
import re
import chardet

def bucket_exists(bucket_name):
    """Verifica se um bucket existe no S3."""
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False

def create_bucket(bucket_name, region=None):
    """Cria um bucket no S3 se ele não existir."""
    if bucket_exists(bucket_name):
        print(f'O bucket "{bucket_name}" já existe.')
        return True
    
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    
    print(f'Bucket "{bucket_name}" criado com sucesso.')
    return True

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
        data_formatada = pd.to_datetime(data, format='%d/%m/%Y', errors='coerce')
        if pd.notna(data_formatada):
            return data_formatada.strftime('%Y-%m-%d')
        else:
            return data
    except ValueError:
        return data

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
    if not bucket_exists(bucket_name):
        print(f'O bucket "{bucket_name}" não existe e será criado.')
        if not create_bucket(bucket_name):
            print("Erro ao criar o bucket. Processo abortado.")
            return
    
    # Verifica se o arquivo corrigido já existe no bucket
    s3_client = boto3.client('s3')
    try:
        s3_client.head_object(Bucket=bucket_name, Key=arquivo_corrigido)
        print(f'O arquivo "{arquivo_corrigido}" já existe no bucket "{bucket_name}".')
    except ClientError:
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

        colunas_para_corrigir = ["Qtd Prejuizos Causados a Uniao"]
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

def query_s3_select(bucket_name, key, query):
    """Executa uma consulta S3 Select no arquivo especificado."""
    s3_client = boto3.client('s3')
    try:
        response = s3_client.select_object_content(
            Bucket=bucket_name,
            Key=key,
            ExpressionType='SQL',
            Expression=query,
            InputSerialization={
                'CSV': {
                    "FileHeaderInfo": "USE",
                    "FieldDelimiter": ";",
                    "QuoteCharacter": "\""
                }
            },
            OutputSerialization={'JSON': {}},
        )

        # Process the payload
        for event in response['Payload']:
            if 'Records' in event:
                print(event['Records']['Payload'].decode('utf-8'))
            elif 'Stats' in event:
                print("Processed Bytes:", event['Stats']['Details']['BytesProcessed'])
            elif 'End' in event:
                print("End of file")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    # Configurações
    bucket_name = 'bucket-da-sprint5-artur'
    arquivo_original = 'PALAS_OPERACOES_2024_01.csv'
    arquivo_corrigido = 'PALAS_OPERACOES_2024_01_corrigido.csv'
    
    # Processar o arquivo e fazer o upload
    processar_arquivo(arquivo_original, arquivo_corrigido, bucket_name)

    # Executar a consulta S3 Select após o upload
    query_file = 'query.sql'
    with open(query_file, 'r', encoding='utf-8') as file:
        query = file.read()
    
    query_s3_select(bucket_name, arquivo_corrigido, query)


