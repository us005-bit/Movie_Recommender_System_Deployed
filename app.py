import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movie_id = i[0]

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.set_page_config(
    page_title="Movie-Recommender",
    page_icon="🎬",
)

st.title('🎬 Movie Recommender')
st.write("Discover your next favorite movie with AI-powered recommendations")


selected_movie_name = st.selectbox(
        '🎯 Choose a Movie You Love',
        movies['title'].values,
        help="Select a movie you enjoyed, and we'll find similar ones for you!"
    )
if st.button('✨ Get Recommendations'):
        with st.spinner('🔮 Analyzing your taste...'):
            import time
            time.sleep(1)

        recommendations = recommend(selected_movie_name)

        # Enhanced recommendations display
        st.write("### 🎪 Movies You'll Love:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"🎬 {i}.{movie}")

        st.snow()
st.write("\n")

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Number of Movies", f"{len(movies):,}")
with col2:
    st.metric("AI Model Used", "Cosine Similarity")