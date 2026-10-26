import streamlit as st
import pickle
import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title='Movie Recommendation System', page_icon='🎬', layout='centered')

logo_path = BASE_DIR / 'assets' / 'logo.png'
if logo_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(str(logo_path), use_container_width=True)

# Load recommendation data
movie_dict = pickle.load(open(BASE_DIR / 'best_model' / 'movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open(BASE_DIR / 'best_model' / 'similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title('🎬 Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select a movie you like:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader("Top 5 Recommended Movies:")
    for j, movie in enumerate(recommendations, 1):
        st.write(f"{j}. {movie}")