import pandas as pd
import streamlit as st

def load_data():
    movies = pd.read_csv("data/movies.csv")
    ratings = pd.read_csv("data/ratings.csv")
    return movies, ratings
