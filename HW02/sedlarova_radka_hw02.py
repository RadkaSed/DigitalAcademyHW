import json


def find_index(word_list, target_word):
    for index, word in enumerate(word_list):
        if word == target_word:
            return index
    return None


def find_decade(year):
    try:
        year = int(year)
        decade = (year // 10) * 10
        return decade
    except ValueError:
        return None
    
    
with open('netflix_titles.tsv', mode='r', encoding='utf-8') as input_file:
    netflix_data = []
    for line in input_file:
        line = line.strip().split('\t')
        if line:
            netflix_data.append(line)



movies_list = []

title_index = find_index(netflix_data[0], 'PRIMARYTITLE')
director_index = find_index(netflix_data[0], 'DIRECTOR')
cast_index = find_index(netflix_data[0], 'CAST')
genres_index = find_index(netflix_data[0], 'GENRES')
startyear_index = find_index(netflix_data[0], 'STARTYEAR')


for line in netflix_data[1:]:
    movie = {}
    movie['title'] = line[title_index]
    if line[director_index]:
        directors_list = line[director_index].split(',')
        clean_directors = []
        for director in directors_list:
            clean_directors.append(director.strip())
        movie['directors'] = clean_directors
    else:
        movie['directors'] = []
    if line[cast_index]:
        cast_list = line[cast_index].split(',')
        clean_cast = []
        for cast in cast_list:
            clean_cast.append(cast.strip())
        movie['cast'] = clean_cast
    else:
        movie['cast'] = []
    if line[genres_index]:
        genres_list = line[genres_index].split(',')
        clean_genres = []
        for genre in genres_list:
            clean_genres.append(genre.strip())
        movie['genres'] = clean_genres
    else:
        movie['genres'] = []
    movie['decade'] = find_decade(line[startyear_index])

    movies_list.append(movie)


with open('hw_02_output.json', mode='w', encoding='utf-8') as output_file:
    json.dump(movies_list, output_file, indent=4)
