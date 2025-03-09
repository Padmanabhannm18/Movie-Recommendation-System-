import streamlit as st
import pandas as pd
from utils import load_data
from content_based import compute_content_similarity, content_based_recommendation
from collaborative import collaborative_filtering

# Load Data
movies, ratings = load_data()
cosine_sim = compute_content_similarity(movies)

# Streamlit UI
st.set_page_config(page_title="Movie Recommendation System", layout="wide", initial_sidebar_state="collapsed")
st.title("🎬 Movie Recommendation System")

st.sidebar.header("Choose Recommendation Model")
model_choice = st.sidebar.radio(
    "Select a model:",
    ["Content-Based Filtering", "Collaborative Filtering"]
)

if model_choice == "Content-Based Filtering":
    st.subheader("📌 Content-Based Filtering")
    movie_title = st.selectbox("Choose a movie:", movies["title"].values)
    if st.button("Get Recommendations (Content-Based)"):
        recommendations = content_based_recommendation(movie_title, cosine_sim, movies)
        if not recommendations.empty:
            st.write("🎥 **Recommended Movies:**")
            st.write(recommendations[["title", "genres"]])
        else:
            st.write("❌ No recommendations found for the selected movie.")

elif model_choice == "Collaborative Filtering":
    st.subheader("📌 Collaborative Filtering")
    user_id = st.selectbox("Choose a User ID:", ratings["userId"].unique())
    if st.button("Get Recommendations (Collaborative)"):
        recommendations = collaborative_filtering(user_id, movies, ratings)
        if not recommendations.empty:
            st.write("🎥 **Recommended Movies:**")
            st.write(recommendations[["title", "genres"]])
        else:
            st.write("❌ No recommendations found for the selected user.")
