import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies [movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]

    recommended_movies = []
    for i in movie_list:
       movie_title =  movies.iloc[i[0]]['original_title']
       recommended_movies.append(movie_title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('What would you like to watch?', movies['original_title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
      st.write(i)
