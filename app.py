import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:6]
    
    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender')

selected_movie = st.selectbox(
    'Enter the name of your movie to get recommendations',
    (movies_list))

if st.button('Recommend'):

    recomendations = recommend(selected_movie)
    for i in recomendations:
        st.write(i)