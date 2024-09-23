from tmdbv3api import TMDb, Movie, Person, Discover
import json
from datetime import datetime
import boto3
import os

tmdb = TMDb()
tmdb.api_key = os.environ['API_KEY'] 
movie = Movie()
person = Person()
discover = Discover()

s3 = boto3.client('s3')

def convert_to_serializable(data):
    if isinstance(data, list):
        return [convert_to_serializable(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_to_serializable(value) for key, value in data.items()}
    elif hasattr(data, '__dict__'):
        return convert_to_serializable(vars(data))
    else:
        return data
        

def get_unique_movies(movie_list):
    seen = set()
    unique_movies = []
    for movie in movie_list:
        movie_id = movie.get('id')  
        if movie_id not in seen:
            seen.add(movie_id)
            unique_movies.append(movie)
    return unique_movies

def get_nolan_movies():
    nolan_results = person.search('Christopher Nolan')
    if not nolan_results:
        return []
    nolan_id = nolan_results[0].id
    nolan_credits = person.movie_credits(nolan_id)
    nolan_movies = []
    for film in nolan_credits.get('crew', []):
        if film['job'] == 'Director':
            movie_details = movie.details(film['id'])
            nolan_movies.append({
                'id': movie_details.get('id'),
                'title': movie_details.get('title'),
                'release_date': movie_details.get('release_date'),
                'popularity': movie_details.get('popularity'),
                'vote_average': movie_details.get('vote_average'),
                'budget': movie_details.get('budget'),
                'revenue': movie_details.get('revenue'),
                'production_companies': [company.get('name') for company in movie_details.get('production_companies', [])]
            })
    return get_unique_movies(nolan_movies)

def get_movies_by_year(year):
    results = discover.discover_movies({
        'primary_release_year': year,
        'sort_by': 'popularity.desc',
        'page': 1
    })
    movies = results.get('results', [])
    movies = [{
        'id': movie.get('id'),
        'title': movie.get('title'),
        'release_date': movie.get('release_date'),
        'popularity': movie.get('popularity'),
        'vote_average': movie.get('vote_average'),
        'budget': movie.get('budget'),
        'revenue': movie.get('revenue')
    } for movie in movies]
    return get_unique_movies(movies)

def get_movies_by_decade(start_year, end_year):
    movies = []
    for year in range(start_year, end_year + 1):
        movies.extend(get_movies_by_year(year))
    return get_unique_movies(movies)

def get_heath_ledger_movies():
    heath_results = person.search('Heath Ledger')
    if not heath_results:
        return []
    heath_id = heath_results[0].id
    heath_movies = person.movie_credits(heath_id)
    movies = []
    for film in heath_movies.get('cast', []):
        movie_details = movie.details(film['id'])
        movies.append({
            'id': movie_details.get('id'),
            'title': movie_details.get('title'),
            'release_date': movie_details.get('release_date'),
            'popularity': movie_details.get('popularity'),
            'vote_average': movie_details.get('vote_average'),
            'budget': movie_details.get('budget'),
            'revenue': movie_details.get('revenue')
        })
    return get_unique_movies(movies)

def save_to_s3(data, bucket, key):
    serializable_data = convert_to_serializable(data)
    s3.put_object(Body=json.dumps(serializable_data), Bucket=bucket, Key=key)

def save_movies_in_files(movies, prefix):
    bucket_name = 'data-lake-artur-mariano-2024'
    for i in range(0, len(movies), 100):
        chunk = movies[i:i+100]
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        filename = f"{prefix}_part_{i//100 + 1}.json"
        s3_key = f"Raw/TMDB/JSON/{year}/{month}/{day}/{filename}"
        save_to_s3(chunk, bucket_name, s3_key)


def lambda_handler(event, context):
    nolan_movies = get_nolan_movies()
    save_movies_in_files(nolan_movies, 'nolan_movies')

    decade_2000_2010 = get_movies_by_decade(2000, 2010)
    save_movies_in_files(decade_2000_2010, 'decade_2000_2010')

    decade_2010_2020 = get_movies_by_decade(2010, 2020)
    save_movies_in_files(decade_2010_2020, 'decade_2010_2020')

    heath_ledger_movies = get_heath_ledger_movies()
    save_movies_in_files(heath_ledger_movies, 'heath_ledger_movies')

    return {
        'statusCode': 200,
        'body': 'Movies data saved successfully!'
    }
