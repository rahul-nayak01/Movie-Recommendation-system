import pickle
import streamlit as st
import pandas as pd


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_name = []
    #recommended_movie_poster = []
    for i in distances[1:6]:
        # fetch the movie poster
        #movie_id = movies.iloc[i[0]].movie_id
        #recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie_name.append(movies.iloc[i[0]].title)

    return recommended_movie_name#,recommended_movie_poster


movies=pickle.load(open('film_dictinory.pkl','rb'))
movies=pd.DataFrame(movies)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name= st.selectbox(
    "Provide suggestion on provided movies",
    movies['title'].values
)

if st.button('Recommendation'):
    recommended_movie_names= recommend(selected_movie_name)
    for i in recommended_movie_names:
        st.write(i)
