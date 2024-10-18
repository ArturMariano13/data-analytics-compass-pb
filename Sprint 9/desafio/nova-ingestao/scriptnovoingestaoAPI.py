import requests
import json
from chaveapi import API_KEY
import time

BASE_URL = 'https://api.themoviedb.org/3'

def get_movies_by_year(year, max_results=100):
    movies = []
    page = 1
    while len(movies) < max_results:
        url = f"{BASE_URL}/discover/movie"
        params = {
            'api_key': API_KEY,
            'primary_release_year': year,
            'sort_by': 'popularity.desc',
            'page': page
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Erro ao buscar filmes de {year}: {response.status_code}")
            break

        results = response.json().get('results', [])

        if not results:
            print(f"Nenhum resultado encontrado para o ano {year} na página {page}.")
            break

        movies.extend(results)

        print(f"Ano {year}: Coletados {len(movies)} filmes até agora...")

        if len(movies) >= max_results:
            movies = movies[:max_results]
            break
        
        page += 1

    return movies

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar detalhes do filme ID {movie_id}: {response.status_code}")
        return None

def get_movie_director(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        credits = response.json()
        crew = credits.get('crew', [])
        for member in crew:
            if member.get('job') == 'Director':
                return member.get('name')
    else:
        print(f"Erro ao buscar diretor do filme ID {movie_id}: {response.status_code}")
    return None

# Função para salvar os dados em blocos de 100
def save_movies_in_chunks(movies, chunk_size=100):
    for i in range(0, len(movies), chunk_size):
        chunk = movies[i:i + chunk_size]
        file_number = i // chunk_size + 1
        output_filename = f'movies_2000_2010_with_directors_part_{file_number}.json'
        with open(output_filename, 'w', encoding='utf-8') as json_file:
            json.dump(chunk, json_file, ensure_ascii=False, indent=4)
        print(f"Salvo '{output_filename}' com {len(chunk)} filmes.")

# Coleta filmes de 2000 a 2010
all_movies = []
for year in range(2000, 2011):
    print(f"Coletando filmes do ano {year}...")
    year_movies = get_movies_by_year(year, max_results=100)
    all_movies.extend(year_movies)
    print(f"Total de filmes coletados até agora: {len(all_movies)} filmes.\n")

# Prepara os dados para salvar em JSON
movies_to_save = []
total_movies = len(all_movies)
start_time = time.time()
for idx, movie in enumerate(all_movies, 1):
    details = get_movie_details(movie.get('id'))
    if details:
        director = get_movie_director(movie.get('id'))
        movies_to_save.append({
            'id': details.get('id'),
            'title': details.get('title'),
            'release_date': details.get('release_date'),
            'popularity': details.get('popularity'),
            'vote_average': details.get('vote_average'),
            'genres': [genre['name'] for genre in details.get('genres', [])],
            'revenue': details.get('revenue'),
            'budget': details.get('budget'),
            'imdb_id': details.get('imdb_id'),
            'director': director
        })
    
    if idx % 10 == 0 or idx == total_movies:
        elapsed_time = time.time() - start_time
        print(f"Processados {idx}/{total_movies} filmes. Tempo decorrido: {elapsed_time:.2f} segundos.")

# Salva os dados em arquivos JSON de até 100 registros
print(f"Iniciando salvamento dos arquivos em chunks...")
save_movies_in_chunks(movies_to_save, chunk_size=100)

print(f"Processo completo!")
