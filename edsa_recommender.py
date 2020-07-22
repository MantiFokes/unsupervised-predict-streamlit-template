"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import random

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    #this function allows for the background colour to be changed 
    # def local_css(file_name):
    #     with open(file_name) as f:
    #         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # local_css('style.css')

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    st.sidebar.header('Movie Recommender Engine')
    page_options = ["Recommender System","Solution Overview","Did you know?", "Suprise me"]
 
    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        
        st.markdown(open('resources/About_solution.md').read())

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    #did you know page
    if page_selection == "Did you know?":
        st.title("Did you know?")
        #top 3 most watched movies
        st.markdown("<h2 style='text-align: left;color: #000000;'>Top 3 most watched movies</h2>", unsafe_allow_html=True)
        st.image('resources/imgs/Top3.PNG', use_column_width= True)
        st.markdown('Watch **[The Shawshank Redemption](https://www.youtube.com/watch?v=6hB3S9bIaco)**')
        st.markdown('Watch **[Forrest Gump](https://www.youtube.com/watch?v=bLvqoHBptjg)**')
        st.markdown('Watch **[Pulp Fiction](https://www.youtube.com/watch?v=s7EdQ4FqbhY)**')

        #word cloud for most common genre
        st.markdown("<h2 style='text-align: left;color: #000000;'>Most watched genres</h2>", unsafe_allow_html=True)
        st.image('resources/imgs/genres.PNG', use_column_width= True)

        #Top 3 per genre
        st.markdown("<h2 style='text-align: left;color: #000000;'>Top 3 most watched movies per genre</h2>", unsafe_allow_html=True)
        genres = ['Comedy','Drama']
        genre_selection = st.radio("What would you like to see?", genres)
        if genre_selection == "Comedy":
            st.write('Hello')

    #suprise me page       
    if page_selection == "Suprise me":
        st.subheader('Here, a movie will be randomly selected for you')
        if st.button('Suprise me'):
            st.write(random.choice(title_list))
            st.balloons()


    #side bar description of app
    st.sidebar.info('This app has been developed by SS4_JHB_Unsupervised team :movie_camera:')        







if __name__ == '__main__':
    main()