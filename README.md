# Movie Recommendation System

A Streamlit application that recommends movies based on a user-selected movie. It leverages a pre-computed similarity matrix and movie list stored as pickle files and fetches movie posters from The Movie Database (TMDb) API.

## Overview

This project uses:
- **Streamlit** for the web interface.
- **Pickle** files (`movie_list.pkl` and `similarity_list.pkl`) for storing movie data and similarity metrics.
- **TMDb API** to fetch movie poster images.
- **Requests** for HTTP operations.

DataSet Link : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## Features

- **Movie Recommendations:** Get recommendations based on a selected movie.
- **Dynamic Poster Fetching:** Automatically fetch and display movie posters.
- **Simple Deployment:** Designed to work seamlessly on platforms like [Streamlit Cloud](https://streamlit.io/cloud) or [Heroku](https://www.heroku.com/).

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation.git
cd movie-recommendation
