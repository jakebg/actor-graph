import tmdbsimple as tmdb
import configparser
import pandas as pd

config = configparser.ConfigParser()
config.read('api.ini')
API = config['DEFAULT']['API']

tmdb.API_KEY = API

movie_list = [603, 245891, 324552 ]

nodes = []
edges = []
repeat_cast = dict()
in_movie = []
titles = []
for a,movie in enumerate(movie_list):
    current_movie = tmdb.Movies(movie)
    dictionary = current_movie.credits()
    cast = [s['name'] for s in dictionary['cast'][:]]   
    title = current_movie.info()['original_title']  
    print(cast)
    for cast_graph in cast:
        if cast_graph not in [person1['name'] for person1 in nodes[:]]:
            nodes.append({'name': cast_graph})
        else:
            print('REPEAT')


print(repeat_cast)

# print([s['name'] for s in nodes[:]])