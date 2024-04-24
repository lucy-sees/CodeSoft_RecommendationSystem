import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    api_key = '4c253fdce964fa58389f2ebeef3048e0'  # Store your API key securely
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
    data = response.json()
    # Check if 'poster_path' key exists in the data
    if 'poster_path' in data:
        return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    else:
        # Return a default or placeholder image URL if 'poster_path' is missing
        return "https://via.placeholder.com/500"  


def recommend(movie):
    movie_index = movies [movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
       movie_id = i[0]
       
       movie_title =  movies.iloc[i[0]]['original_title']
       movie_poster = fetch_poster(i[0])

       recommended_movies.append(movie_title)
       recommended_movies_posters.append(movie_poster)
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

movie_list = movies['original_title'].values
selected_movie_name = st.selectbox('What would you like to watch?', movie_list)

if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        print(recommended_movie_posters[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
