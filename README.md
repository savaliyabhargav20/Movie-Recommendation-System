# 🎬 Movie Recommendation System

A Python-based Movie Recommendation System that helps users discover movies similar to the ones they like. It uses machine learning techniques to compare movie information and recommend related movies based on their content.

## 📌 Project Overview

Finding a good movie to watch can take time. This project makes it easier by suggesting similar movies based on details such as genres, keywords, cast, crew, and movie descriptions.

The system uses **Content-Based Filtering** with `CountVectorizer` and `Cosine Similarity` to find movies with similar features.

## ✨ Features

- 🎥 **Movie Recommendations:** Suggests similar movies based on a selected movie.
- 🔍 **Content-Based Filtering:** Uses movie information to find related titles.
- 🧹 **Data Preprocessing:** Cleans and combines movie and credits datasets.
- 🤖 **Machine Learning:** Uses text feature extraction and cosine similarity.
- 📊 **TMDB Dataset:** Works with movie details and cast information.
- ⚡ **Fast Recommendations:** Saves processed data and similarity results using Python pickle files.
- 🎯 **Relevant Results:** Finds movies with similar content to the selected movie.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading and processing |
| NumPy | Numerical operations |
| Scikit-learn | Feature extraction and similarity calculation |
| CountVectorizer | Converts movie text into numerical features |
| Cosine Similarity | Measures similarity between movies |
| Pickle | Saves and loads processed data and model results |
| TMDB Dataset | Provides movie information and credits |

## 📂 Dataset

This project uses the TMDB 5000 Movie Dataset.

Required dataset files:

- `tmdb_5000_movies.csv` — contains movie titles, genres, keywords, overviews, and other details.
- `tmdb_5000_credits.csv` — contains cast and crew information.

Place both files inside the `datasets` folder.

## ⚙️ How It Works

1. **Load the data:** Read the movie and credits CSV files using Pandas.
2. **Combine datasets:** Merge movie details with cast and crew information.
3. **Clean the data:** Handle missing values and process selected features.
4. **Create movie tags:** Combine useful information such as genres, keywords, cast, crew, and overview.
5. **Extract features:** Use `CountVectorizer` to convert text into numerical vectors.
6. **Calculate similarity:** Use cosine similarity to compare movies.
7. **Generate recommendations:** Find the most similar movies and return the top results.
8. **Save processed data:** Use Pickle to store the processed movie data and similarity matrix for later use.

## 📥 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/savaliyabhargav20/Movie-Recommendation-System.git
```

### 2. Open the project folder

```bash
cd Movie-Recommendation-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 4. Install the required libraries

```bash
pip install pandas numpy scikit-learn
```

If your project uses Streamlit or other libraries, install those too. If a `requirements.txt` file is available, you can install all listed dependencies with:

```bash
pip install -r requirements.txt
```

### 5. Add the dataset

Create a folder named `datasets` and place the two CSV files inside it:

```text
datasets/
├── tmdb_5000_movies.csv
└── tmdb_5000_credits.csv
```

### 6. Run the project

Run the Python file that contains your model-building code:

```bash
python your_training_file.py
```

If your project has a Streamlit interface, start it using the actual application filename, for example:

```bash
streamlit run app.py
```

**Note:** Replace `your_training_file.py` and `app.py` with the actual filenames in your repository. Generate any required Pickle files before starting an application that loads them.

## 📁 Project Structure

The following is an example structure for this project. Adjust it to match the files in your repository.

```text
Movie-Recommendation-System/
│
├── datasets/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── main.py                 # Model training or data processing
├── app.py                  # Application interface, if included
├── movie_list.pkl          # Processed movie data, if generated
├── similarity.pkl          # Similarity matrix, if generated
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Files excluded from Git
```

## 🧪 Example

Suppose a user selects **The Dark Knight**.

The recommendation system compares its available features with other movies and returns titles that have similar content.

The recommendations depend on the dataset and the features selected during preprocessing.

## 🎯 Learning Outcomes

By building this project, you can learn:

- How to work with real-world CSV datasets.
- How to clean and prepare movie data.
- How content-based recommendation systems work.
- How to convert text into numerical features.
- How cosine similarity finds related items.
- How to save and load data using Pickle.
- How Python and machine learning can be used to build useful applications.

## 🚀 Future Improvements

- Add a search box for movie titles.
- Display movie posters and ratings.
- Build a responsive web interface.
- Add filters for genre, language, and release year.
- Include user ratings and personalized recommendations.
- Deploy the application online.

## 👨‍💻 Author

**Bhargav Savaliya**

- GitHub: [@savaliyabhargav20](https://github.com/savaliyabhargav20)
- Project Repository: [Movie Recommendation System](https://github.com/savaliyabhargav20/Movie-Recommendation-System)

## 📄 License

This project is intended for learning and educational purposes. Add a license file to the repository if you want to specify the terms under which others may use or modify your code.

---

⭐ If you find this project useful, consider giving the repository a star!
