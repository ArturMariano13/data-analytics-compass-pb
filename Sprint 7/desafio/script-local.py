from tmdbv3api import TMDb, Movie, Person
import json
from secrets import API_KEY

# Configurando TMDB
tmdb = TMDb()
tmdb.api_key = API_KEY  


movie = Movie()
person = Person()

# Função para obter os filmes dirigidos por Christopher Nolan e salvar em JSON
def get_director_movies_to_json(director_name, max_size_mb=10):
    # Buscar pelo ID do diretor
    director = person.search(director_name)
    
    if director:
        director_id = director[0].id  # Pega o ID do primeiro resultado (Christopher Nolan)
        print(f"Encontrado {director_name} com ID: {director_id}")
        
        # Buscar todos os créditos do diretor
        credits = person.movie_credits(director_id)

        # Lista para armazenar os detalhes dos filmes
        directed_movies = []
        
        # Buscar detalhes de cada filme onde ele foi diretor
        for crew_member in credits.crew:
            if crew_member['job'] == 'Director':
                # Obter detalhes do filme usando o ID
                movie_details = movie.details(crew_member['id'])
                
                # Adicionar os detalhes relevantes, incluindo orçamento e receita
                directed_movies.append({
                    'title': movie_details.title,
                    'release_date': movie_details.release_date,
                    'overview': movie_details.overview,
                    'vote_average': movie_details.vote_average,
                    'vote_count': movie_details.vote_count,
                    'popularity': movie_details.popularity,
                    'budget': movie_details.budget,  # Orçamento do filme
                    'revenue': movie_details.revenue,  # Receita do filme
                    'genres': [genre['name'] for genre in movie_details.genres]  # Converte os gêneros em uma lista de strings
                })

        # Converte a lista de filmes em JSON
        json_data = json.dumps(directed_movies, indent=4)
        
        # Verifica o tamanho do JSON gerado
        json_size_mb = len(json_data.encode('utf-8')) / (1024 * 1024)  # Converte o tamanho para MB
        
        if json_size_mb > max_size_mb:
            print(f"O tamanho do JSON é {json_size_mb:.2f} MB, excedendo o limite de {max_size_mb} MB.")
            # Limitar o número de filmes para reduzir o tamanho do arquivo
            limit = int(len(directed_movies) * (max_size_mb / json_size_mb))
            limited_movies = directed_movies[:limit]
            
            # Recriar o JSON com a lista limitada
            json_data = json.dumps(limited_movies, indent=4)
            print(f"O arquivo foi reduzido para {len(limited_movies)} filmes.")
        
        # Salvar o JSON em um arquivo
        with open('nolan_movies.json', 'w') as f:
            f.write(json_data)
        
        print(f"JSON salvo com sucesso! Tamanho final: {len(json_data.encode('utf-8')) / (1024 * 1024):.2f} MB")
    else:
        print(f"Diretor {director_name} não encontrado.")

# Buscar filmes dirigidos por Christopher Nolan e salvar em JSON
get_director_movies_to_json("Christopher Nolan")