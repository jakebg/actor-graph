import tmdbsimple as tmdb
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('api.ini')
API = config['DEFAULT']['API']

tmdb.API_KEY = API

movie_list = [603, 245891, 324552 ]

full_list = []
in_movie = []
main_nodes = []
for j,movie in enumerate(movie_list):
    current_movie = tmdb.Movies(movie)
    dictionary = current_movie.credits()
    cast = [s['name'] for s in dictionary['cast'][:]]   
    title = current_movie.info()['original_title']  
    print(title)
    for cast_graph in cast:
        if cast_graph not in [person1['name'] for person1 in full_list[:]]:
            full_list.append({'name': cast_graph,'movie': title, 'count': 1})
        else:
            print('REPEAT')

   
#print([s['name'] for s in full_list[:]])
test = pd.DataFrame(full_list)
print(test)


# check through total cast
# find out who has most appearences in each movie
# they are main nodes 