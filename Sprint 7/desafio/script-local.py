from tmdbv3api import TMDb, Movie
import requests
import boto3
import json
import os
from datetime import datetime

# Configurando TMDB
tmdb = TMDb()
tmdb.api_key = os.getenv('TMDB_API_KEY')  # Armazene a chave de API em uma variável de ambiente

movie = Movie()

def get_movie_details(movie_id):
    details = movie.details(movie_id)
    return details

# Função para salvar os dados no S3
def save_to_s3(data, bucket_name, path):
    s3_client = boto3.client('s3')
    json_data = json.dumps(data, indent=4)
    s3_client.put_object(Bucket=bucket_name, Key=path, Body=json_data)

def lambda_handler(event, context):
    bucket_name = 'data-lake-artur-mariano'
    now = datetime.now()
    data_atual = now.strftime('%Y/%m/%d')

    # IDs de filmes que você quer complementar (pode ser obtido dos arquivos CSV)
    movie_ids = [550, 578, 597]  # Exemplo de IDs de filmes do TMDB

    # Captura de dados
    dados_filmes = []
    for movie_id in movie_ids:
        detalhes = get_movie_details(movie_id)
        dados_filmes.append(detalhes)

        # Agrupar arquivos em lotes de 100
        if len(dados_filmes) >= 100:
            file_name = f"Raw/TMDB/JSON/{data_atual}/filmes_{now.strftime('%H%M%S')}.json"
            save_to_s3(dados_filmes, bucket_name, file_name)
            dados_filmes.clear()  # Limpar para o próximo grupo

    # Salvar o restante dos dados
    if dados_filmes:
        file_name = f"Raw/TMDB/JSON/{data_atual}/filmes_{now.strftime('%H%M%S')}.json"
        save_to_s3(dados_filmes, bucket_name, file_name)
