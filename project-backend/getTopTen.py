import numpy as np
import ast
import pytz
import math
import itertools
from sklearn.preprocessing import LabelBinarizer
import pandas as pd
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Compute the cosine similarity matrix






def get_recommendations(name):
    df = pd.read_csv('top10K-spotify.csv',index_col=0)
    df["type"].value_counts()
    df=df.drop(columns=["index","city_1","district_1","district_2","city_3","district_3" ])
    df = df[df['city_2'].notna()]
    df = df[df['country'].notna()]
    df.rename(columns = {'artist':'name'}, inplace = True)
    # print(data_df.head())

    df2=pd.read_csv('data_w_spotify.csv',index_col=None)
    df2=df2.drop(columns=["isdone","id"])
    df2['genres'] = df2['genres'].fillna('')

    df3=df.merge(df2,on='name')


    df3['genres']= df3['genres'].str.strip('[]').str.replace("'","").str.split('\s*,\s*')

    def create_soup(x):
        return ' '.join(x['genres']) + ' ' + ' '+ x['city_2'] + ' ' + x['country']+' ' + x['gender']+' ' + x['type']

    df3['soup'] = df3.apply(create_soup, axis=1)

    count = CountVectorizer()
    count_matrix = count.fit_transform(df3['soup'])
    # print(df3.head())
    # print(count_matrix.shape)
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    dict_names = dict(zip(df3.name, df3.spotifyid))
    df3=df3.drop(columns=["spotifyid"])
    # Get the index of the movie that matches the title
    df3 = df3.reset_index()
    indices = pd.Series(df3.index, index=df3['name']).drop_duplicates()
    idx = indices[name]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]
    # print(sim_scores)

    # Get the movie indices
    indices = [i[0] for i in sim_scores]
    scores = [round(i[1]*100, 2) for i in sim_scores]

    # Return the top 10 most similar movies
     
    top_10=df3['name'].iloc[indices]
    spot_top10=[]
    for item in top_10:
        spot_top10.append(dict_names[str(item)])

    artist=dict_names[str(df3['name'].iloc[idx])]\
    
    wantedDict = {
        'mainId': artist,
        'top10': spot_top10,
        'scores': scores
    }

    return wantedDict
