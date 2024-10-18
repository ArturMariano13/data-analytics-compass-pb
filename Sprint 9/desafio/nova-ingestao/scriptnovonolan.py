import requests
import json
from chaveapi import API_KEY

BASE_URL = 'https://api.themoviedb.org/3'

def search_director_movies(director_name, max_results=100):
    # Busca o ID do diretor
    search_url = f"{BASE_URL}/search/person"
    params = {
        'api_key': API_KEY,
        'query': director_name,
        'language': 'pt-BR'
    }
    
    response = requests.get(search_url, params=params)
    
    if response.status_code != 200:
        print(f"Erro ao buscar o diretor: {response.status_code}")
        return []

    director_id = None
    results = response.json().get('results', [])
    for person in results:
        if person.get('name') == director_name:
            director_id = person.get('id')
            break

    if director_id is None:
        print(f"Diretor '{director_name}' não encontrado.")
        return []

    # Busca os filmes do diretor
    movies_url = f"{BASE_URL}/person/{director_id}/movie_credits"
    params = {
        'api_key': API_KEY,
        'language': 'pt-BR'
    }

    response = requests.get(movies_url, params=params)

    if response.status_code != 200:
        print(f"Erro ao buscar filmes do diretor: {response.status_code}")
        return []

    movies = response.json().get('crew', [])
    
    # Filtra apenas os filmes que ele dirigiu
    nolan_movies = [
        movie['id']
        for movie in movies if movie['job'] == 'Director'
    ]

    # Obter detalhes completos para cada filme
    detailed_movies = []
    for movie_id in nolan_movies[:max_results]:  # Limita o número de filmes retornados
        details = get_movie_details(movie_id, director_name)
        if details:
            detailed_movies.append(details)

    return detailed_movies

def get_movie_details(movie_id, director_name):
    # Busca detalhes completos do filme
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        'api_key': API_KEY
        }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return {
            'id': response.json().get('id'),
            'title': response.json().get('title'),
            'release_date': response.json().get('release_date'),
            'popularity': response.json().get('popularity'),
            'vote_average': response.json().get('vote_average'),
            'genres': [genre['name'] for genre in response.json().get('genres', [])],  # Nome dos gêneros
            'revenue': response.json().get('revenue'),
            'budget': response.json().get('budget'),
            'imdb_id': response.json().get('imdb_id'),
            'director': director_name  # Adiciona o nome do diretor manualmente
        }
    else:
        print(f"Erro ao buscar detalhes do filme ID {movie_id}: {response.status_code}")
        return None

def save_movies_to_json(movies, filename='nolan_movies.json'):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(movies, json_file, ensure_ascii=False, indent=4)
    print(f"Filmes salvos em '{filename}' com sucesso.")

def main():
    director_name = "Christopher Nolan"
    print(f"Buscando filmes do diretor {director_name}...")
    nolan_movies = search_director_movies(director_name)

    if nolan_movies:
        # Salva os filmes em um arquivo JSON
        save_movies_to_json(nolan_movies)

if __name__ == "__main__":
    main()
