import pickle
import streamlit as st 
import requests

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances  = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x:x[1])
    recommendedMoviesName, recommendedMoviesPoster = [], []
    for i in distances[1:11] :
        movie_id = movies.iloc[i[0]].id
        recommendedMoviesName.append(movies.iloc[i[0]].title)
        recommendedMoviesPoster.append(fetchPoster(movie_id))
    return recommendedMoviesName, recommendedMoviesPoster    

def fetchPoster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
st.header("Movie Recommendation System")
st.write("This app will recommend movies based on your favorite movie")

movies = pickle.load(open("artifacts/movie_list.pkl", "rb"))
similarity = pickle.load(open("artifacts/similarity_list.pkl", "rb"))

movies_list = movies['title'].values

selected_movie = st.selectbox(
    'Type movie name',
    movies_list
)

if st.button("Recommend"):
    recommendedMoviesName, recommendedMoviesPoster = recommend(selected_movie)
    
    # Display the movies in rows of 5
    for i in range(0, len(recommendedMoviesName), 5):
        cols = st.columns(5)
        
        for j, col in enumerate(cols):
            if i + j < len(recommendedMoviesName):
                col.text(recommendedMoviesName[i + j])
                col.image(recommendedMoviesPoster[i + j])
