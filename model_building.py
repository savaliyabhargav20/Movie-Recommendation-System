import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 1. Load datasets
movies = pd.read_csv(BASE_DIR / 'datasets' / 'tmdb_5000_movies.csv')
credits = pd.read_csv(BASE_DIR / 'datasets' / 'tmdb_5000_credits.csv')
movies = movies.merge(credits, on='title')


# 2. Select relevant features & handle missing values
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies = movies.dropna()

# Helper function to parse JSON-like columns
def convert(obj):
    return [i['name'] for i in ast.literal_eval(obj)]

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def convert_cast(obj):
    counter = 0
    l = []
    for i in ast.literal_eval(obj):
        if counter != 3:
            l.append(i['name'])
            counter += 1
        else:
            break
    return l

movies['cast'] = movies['cast'].apply(convert_cast)

def fetch_director(obj):
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            return [i['name']]
    return []

movies['crew'] = movies['crew'].apply(fetch_director)
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces between names (e.g., "Sam Worthington" -> "SamWorthington")
for col in ['genres', 'keywords', 'cast', 'crew']:
    movies[col] = movies[col].apply(lambda x: [i.replace(" ", "") for i in x])

# Create 'tags' column
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
new_df = movies[['movie_id', 'title', 'tags']]
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x).lower())

# 3. Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# 4. Calculate Similarity Matrix
similarity = cosine_similarity(vectors)

# 5. Export to pickle files
best_model_dir = BASE_DIR / 'best_model'
best_model_dir.mkdir(parents=True, exist_ok=True)
pickle.dump(new_df.to_dict(), open(best_model_dir / 'movie_dict.pkl', 'wb'))
pickle.dump(similarity, open(best_model_dir / 'similarity.pkl', 'wb'))
print("Pickle files generated successfully!")
