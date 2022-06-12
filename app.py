from urllib import response
import pandas as pd
import pickle
import streamlit as st
import requests  


def getPoster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e7b02e41e52bbb21f7ea7407f50acc5e&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    
    recommended_list = []
    recommended_posters = []
    for i in distances[1:6]:
        recommended_list.append(movies.iloc[i[0]].title)
        recommended_posters.append(getPoster(movies.iloc[i[0]].movie_id))
    return recommended_list, recommended_posters

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
st.title('Movie Recommender')

selected_option = st.selectbox("Select your Movie", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
