import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def collaborative_filtering(user_id, movies, ratings):
    user_item_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    user_sim = cosine_similarity(user_item_matrix)  # User similarity matrix
    user_idx = user_id - 1  # User index (assuming user IDs start from 1)
    similar_users = np.argsort(-user_sim[user_idx])[1:6]  # Top 5 similar users

    watched_movies = ratings[ratings['userId'] == user_id]['movieId'].values
    similar_users_movies = ratings[ratings['userId'].isin(similar_users)]['movieId']
    recommendations = similar_users_movies[~similar_users_movies.isin(watched_movies)].unique()[:5]

    return movies[movies['movieId'].isin(recommendations)]
