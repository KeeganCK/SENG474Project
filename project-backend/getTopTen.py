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
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from num2words import num2words

df = pd.read_csv('top10K-spotify.csv',index_col=0)
df["type"].value_counts()
df=df.drop(columns=["index","city_1","district_1","district_2","city_3","district_3" ])
df = df[df['city_2'].notna()]
df = df[df['country'].notna()]
df.rename(columns = {'artist':'name'}, inplace = True)

df2=pd.read_csv('data_w_spotify.csv',index_col=None)
df2=df2.drop(columns=["isdone","id"])
df2['genres'] = df2['genres'].fillna('')

df3=df.merge(df2,on='name')
df3['age']=df3["age"].apply(lambda x: num2words(round(x/10)*10))
df3['popularity']=df3["popularity"].apply(lambda x: num2words(round(x/10)*10))


df3['genres']= df3['genres'].str.strip('[]').str.replace("'","").str.split('\s*,\s*')
df3['genres'] = df3.apply(lambda x:' '.join(x['genres']) + ' '+ x['city_2'] + ' ' + x['country']+' ' + x['gender']+' ' + x['type']+' '+x['age']+ ' '+ x['popularity'], axis=1)

print(df3.shape,df3.columns)

dict_names = dict(zip(df3.name, df3.spotifyid))

df3 = df3.reset_index()
indices = pd.Series(df3.index, index=df3['name']).drop_duplicates()



def get_recommendations(name,sim,reverse):
    # print(sim[0:20])
    # print(name,sim)
    indices = pd.Series(df3.index, index=df3['name']).drop_duplicates()
    idx = indices[name]

    # Get the pairwsie similarity scores of all artsits with that movie
    sim_scores = list(enumerate(sim[idx]))
    if not isinstance(sim_scores[0][1],np.ndarray):
        # Sort the artists based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=reverse)

        # Get the scores of the 10 most similar artsits
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        indices = [i[0] for i in sim_scores]
        scores = [round(i[1]*100, 2) for i in sim_scores]

        # Return the top 20 most similar artsits
        top_10=df3['name'].iloc[indices]
        spot_top10=[]
        spot_top10_names=[]
        for item in top_10:
            spot_top10_names.append(item)
            spot_top10.append(dict_names[str(item)])

        artist=dict_names[str(df3['name'].iloc[idx])]
        
        wantedDict = {
            'mainId': artist,
            'top10': spot_top10,
            'scores': scores
        }

    return wantedDict

def CVectorizer():
    count = CountVectorizer()
    count_matrix = count.fit_transform(df3['genres'])
    return count_matrix

def CosSim(x):
    return (cosine_similarity(x,x),True)

def TfidVectorizer():
    count = TfidfVectorizer()
    count_matrix = count.fit_transform(df3['genres'])
    return count_matrix

def EuDSim(x):
    return (euclidean_distances(x,), False)