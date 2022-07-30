import pandas as pd
import streamlit as st
import pickle
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# Load the pickle files
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity_matrix = pickle.load(open('similarity_matrix.pkl', 'rb'))

# Create a dataframe
movies = pd.DataFrame(movie_dict)

html_temp = """ 
<div style = "background-color: #63e0c7; padding: 10px">
<h2 style = "color: white; text-align: center;">Movie Recommender System
</div>
<div style = "background-color: white; padding: 5px">
<p style= "color: #099e80; text-align: center; font-family: Courier; font-size: 15px;">
<i>Not sure what to watch next? Let's recommend you something...</i></p>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)


image_path = 'img1.jpg'
image = Image.open(image_path)
st.image(image, use_column_width=True)


selected_movie = st.selectbox("What are you looking for today?", movies['title'].values)
st.write('You selected:', selected_movie)


def recommend(movie):
    # Get index of a movie
    movie_index = movies[movies['title'] == movie].index[0]
    # To get the distance with every other movie, we need to get its index in the similarity matrix
    distances = similarity_matrix[movie_index]
    # Sort the movies acc to similarity
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    # Fetch the top 10 similar movies
    recommended_movies = []
    for i in movies_list[1:11]:
        movie_id = movies.iloc[i[0]]
        recommended_movies.append(movie_id.title)
    return recommended_movies


if st.button('Show Recommendations'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)


html_temp1 = """
    <div style = "background-color: #63e0c7">
    <p style = "color: white; text-align: center;">Designed & Developed By: <b>Rajashri Deka</b></p>
    </div>
    """
st.markdown(html_temp1,unsafe_allow_html=True)