def loadCSV(filename):
    def parse_line(line):
        fields = []
        field = ""
        inside_quotes = False
        
        for char in line:
            if char == '"':
                inside_quotes = not inside_quotes
            elif char == ',' and not inside_quotes:
                fields.append(field)
                field = ""
            else:
                field += char
        
        fields.append(field)
        return fields
    
    keys = []
    data = []
    
    with open(filename, 'r') as file:
        keys = parse_line(file.readline().strip())
        
        for line in file:
            values = parse_line(line.strip())
            if len(values) == len(keys):
                actor_dict = dict(zip(keys, values))
                data.append(actor_dict)
    
    return data

def most_movies_actor(actors):

    max_actor = None
    max_movies = 0

    for actor in actors:
        try:
            num_movies = int(actor.get('Number of Movies', 0))
        except ValueError:
            continue

        if num_movies > max_movies:
            max_movies, max_actor = num_movies, actor

    return f"{max_actor.get('Actor')} - {max_actor.get('Number of Movies')}"

def gross_media(actors):    
    total_gross = 0.0
    count = 0

    for actor in actors:
        try:
            gross = float(actor.get('Gross', 0.0)) 
            total_gross += gross
            count += 1
        except ValueError:
            continue
    
    return round(total_gross / count, 2)


def biggest_avg_movie_actor(actors):
    max_actor = None
    max_avg = 0.0

    for actor in actors:
        try:
            avg = float(actor.get('Average per Movie', 0.0))
        except ValueError:
            continue

        if avg > max_avg:
            max_avg, max_actor = avg, actor

    return f"{max_actor.get('Actor')} - {max_actor.get('Average per Movie')}"

def most_ticket_movies(actors):
    movie_count = {}
    
    for actor in actors:
        movie = actor.get('#1 Movie', '')
        if movie:
            if movie in movie_count:
                movie_count[movie] += 1
            else:
                movie_count[movie] = 1

    movie_list = [(movie, count) for movie, count in movie_count.items()]

    # x é o parâmetro de ordenação ([1] é a quantidade de aparições e 0 é o nome do filme) 
    movie_list.sort(key=lambda x: (-x[1], x[0]))

    result = [f"{index + 1} - O filme {movie} aparece {count} vez(es) no dataset" for index, (movie, count) in enumerate(movie_list)]

    return result


def actors_order_by_total_gross(actors):    
    actors_total_gross = [{'Actor': actor['Actor'], 'Total Gross': actor['Total Gross']} for actor in actors]

    sorted_data = sorted(actors_total_gross, key=lambda x: x['Total Gross'], reverse=True)
    return '\n'.join(f"{actor['Actor']} - {actor['Total Gross']}" for actor in sorted_data)

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    try:
        filename = 'actors.csv'
        data = loadCSV(filename)

        most_movies_result = most_movies_actor(data)
        write_to_file('etapa-1.txt', most_movies_result)

        gross_media_result = gross_media(data)
        write_to_file('etapa-2.txt', str(gross_media_result))

        biggest_avg_movie_actor_result = biggest_avg_movie_actor(data)
        write_to_file('etapa-3.txt', biggest_avg_movie_actor_result)

        most_ticket_movies_result = most_ticket_movies(data)
        write_to_file('etapa-4.txt', '\n'.join(most_ticket_movies_result))

        actors_order_by_total_gross_result = actors_order_by_total_gross(data)
        write_to_file('etapa-5.txt', actors_order_by_total_gross_result)

        print("Programa finalizado com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()

