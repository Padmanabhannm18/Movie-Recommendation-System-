import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

@st.cache_data
def compute_content_similarity(movies):
    tfidf = TfidfVectorizer(stop_words="english")
    movies["genres"] = movies["genres"].fillna("")
    tfidf_matrix = tfidf.fit_transform(movies["genres"])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

def content_based_recommendation(movie_title, cosine_sim, movies):
    try:
        idx = movies[movies['title'] == movie_title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        movie_indices = [i[0] for i in sim_scores]
        return movies.iloc[movie_indices]
    except IndexError:
        return pd.DataFrame(columns=["title", "genres"])
