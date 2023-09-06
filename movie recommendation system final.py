import pandas as pd
import re
import numpy as np
import tkinter as tk
from tkinter import ttk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data
movies = pd.read_csv(r"C:\Users\chatu\movies.csv")

# Clean movie titles
def clean_title(title):
    title = re.sub("[^a-zA-Z0-9 ]", "", title)
    return title

movies["clean_title"] = movies["title"].apply(clean_title)

# Create TF-IDF vectors for movie titles
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf = vectorizer.fit_transform(movies["clean_title"])

# Function to find similar movies
def find_similar_movies(movie_id):
    similar_users = ratings[(ratings["movieId"] == movie_id) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)

    similar_user_recs = similar_user_recs[similar_user_recs > 0.10]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    return rec_percentages.head(10).merge(movies, left_index=True, right_on="movieId")[["score", "title", "genres"]]

# Create a tkinter GUI
root = tk.Tk()
root.title("Movie Recommendation System")

# Function to handle movie recommendations
def recommend_movies():
    input_title = movie_input.get()
    if len(input_title) > 5:
        query_vec = vectorizer.transform([clean_title(input_title)])
        similarity = cosine_similarity(query_vec, tfidf).flatten()
        indices = np.argpartition(similarity, -5)[-5:]
        results = movies.iloc[indices].iloc[::-1]
        recommended_movie_id = results.iloc[0]["movieId"]
        recommended_movies = find_similar_movies(recommended_movie_id)
        result_text.set(recommended_movies[["title", "genres"]].to_string(index=False))

# Movie input label and entry
movie_label = ttk.Label(root, text="Enter a Movie Title:")
movie_label.pack()
movie_input = ttk.Entry(root)
movie_input.pack()

# Recommend button
recommend_button = ttk.Button(root, text="Recommend Movies", command=recommend_movies)
recommend_button.pack()

# Result label
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text)
result_label.pack()

# Load ratings data (you should replace this with your actual ratings data)
ratings = pd.read_csv(r"C:\Users\chatu\ratings.csv")

root.mainloop()
