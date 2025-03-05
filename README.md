# 🎮 Movie Recommendation System

## 📌 Project Overview
This project is a **Movie Recommendation System** that suggests movies based on **two approaches**:
1. **Content-Based Filtering** - Recommends movies similar to a selected movie using genre-based TF-IDF vectorization.
2. **Collaborative Filtering** - Suggests movies to a user based on ratings given by similar users.

## 🏷️ Project Structure
```
movie_recommendation_system/
│── main.py                  # Main Streamlit UI
│── content_based.py          # Content-based filtering logic
│── collaborative.py          # Collaborative filtering logic
│── utils.py                  # Utility functions
│── data/                     # Dataset folder (movies.csv, ratings.csv)
│── requirements.txt          # Dependencies
│── README.md                 # Project Documentation
```

## 🔧 Installation and Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## 🚀 Running the Application

After installing dependencies, run the Streamlit app:
```sh
streamlit run main.py
```

## 📂 Code Structure

### `main.py`
- **Streamlit UI** for selecting the recommendation model.
- Allows users to choose between **Content-Based Filtering** and **Collaborative Filtering**.
- Displays recommended movies based on user selection.

### `content_based.py`
- **Computes movie similarity** using **TF-IDF vectorization**.
- Returns a list of movies similar to the one selected by the user.

### `collaborative.py`
- **User-based collaborative filtering** using **cosine similarity**.
- Identifies similar users and recommends movies they liked.

### `utils.py`
- Loads movie and rating datasets.
- Provides utility functions for data processing.

### `data/`
- **movies.csv** - Contains movie IDs, titles, and genres.
- **ratings.csv** - Contains user ratings for movies.

## 🎯 Features
✅ **Content-Based Filtering** using movie genres.  
✅ **Collaborative Filtering** based on similar users' preferences.  
✅ **Interactive UI** using Streamlit.  
✅ **Efficient recommendations** using TF-IDF and cosine similarity.  

## 📌 Example Output
- **Selected Movie:** The Matrix 🎥
- **Recommended Movies:**
  - Inception
  - Blade Runner 2049
  - Interstellar

OR

- **User ID:** 5
- **Recommended Movies:**
  - The Dark Knight
  - The Lord of the Rings
  - Gladiator

## 👨‍💻 Contributing
Feel free to contribute by improving the recommendation algorithms!
1. Fork the repo
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a Pull Request

## 🛠️ Technologies Used
- **Python** 🐍
- **Streamlit** 📊
- **Scikit-learn** 🤖
- **TF-IDF Vectorization** 🔠
- **Cosine Similarity** 📏
- **NumPy & Pandas** 📊

## 🐝 License
This project is open-source and available under the **MIT License**.

---

🎮 **Happy Coding!** 🚀

