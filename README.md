# Movie Recommendation System

This project implements a simple movie recommendation system using Python. It utilizes the `pandas`, `re`, `numpy`, `tkinter`, and `scikit-learn` libraries to provide movie recommendations based on user input. The system loads and preprocesses movie data, calculates TF-IDF vectors for movie titles, and suggests similar movies.

## Setup

Ensure you have the required libraries installed:

```
pip install pandas re numpy scikit-learn
```

## Getting Started

1. Clone or download the project to your local machine.

2. Replace the following placeholders in the script with your data:
   - `movies.csv`: Replace with your movie dataset file path.
   - `ratings.csv`: Replace with your movie ratings dataset file path.

3. Run the script using a Python interpreter.

## How It Works

1. **Data Loading**: Movie data is loaded from a CSV file into a pandas DataFrame.

2. **Data Cleaning**: Movie titles are cleaned by removing non-alphanumeric characters and converting to lowercase.

3. **TF-IDF Vectorization**: TF-IDF vectors are created for movie titles to represent their content.

4. **Similarity Calculation**: The script calculates the cosine similarity between the input movie title and all movie titles in the dataset. It recommends movies with the highest similarity scores.

5. **GUI**: A tkinter GUI allows users to input a movie title and receive movie recommendations based on similarity.

## Usage

1. Launch the script to open the GUI titled "Movie Recommendation System."

2. Enter a movie title (minimum 5 characters) in the provided text field.

3. Click "Recommend Movies."

4. The recommended movies, along with their genres, will be displayed in the result area.

## Note

- Replace the file paths for `movies.csv` and `ratings.csv` with your dataset files.

- Ensure that your dataset includes at least two columns: `title` for movie titles and `movieId` for unique movie identifiers.

- This is a basic recommendation system; you can enhance it by using more advanced techniques and larger datasets.

Feel free to customize and expand the project to meet your specific project requirements and dataset characteristics.
