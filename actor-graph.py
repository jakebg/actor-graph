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
        full_list.append({'name': cast_graph,'movie': title})


   
#print([s['name'] for s in full_list[:]])
df_actor = pd.DataFrame(full_list)
value_counts = df_actor['name'].value_counts()
df_vc = value_counts.rename_axis('names').reset_index(name='count')
print(df_vc)

repeat_actors = []
for index,row in df_vc.iterrows():
    if (row['count'] > 1):
        print(row['names'])
        repeat_actors.append(row['names'])
print(repeat_actors)
