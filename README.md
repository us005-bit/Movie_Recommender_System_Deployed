# 🎬 Movie Recommender System

>An intelligent movie recommendation system built with Python and Streamlit that suggests movies based on content similarity using machine learning algorithms. This is my first deployable project showcasing end-to-end machine learning implementation.

Live Demo
https://movie-recommender-system0.streamlit.app/

#Features

- 🎯 Content-Based Filtering: Recommends movies based on genre, cast, and crew similarity
- 🖥️ Interactive Web Interface: Clean and intuitive Streamlit web application
- ⚡ Real-time Recommendations: Get instant movie suggestions with just one click
- 📊 Large Dataset: Trained on comprehensive movie database with almost 5000 movies
- 🔍 Smart Search: Easy movie selection with searchable dropdown

#Technologies Used

Python - Core programming language
Streamlit - Web application framework
Pandas - Data manipulation and analysis
Scikit-learn - Machine learning algorithms
Pickle - Model and data serialization

#Platforms Used
Jupyter Notebook - Machine Learning Algorithm
PyCharm - Streamlit Code

#How It Works

Algorithm Overview
The system uses Content-Based Filtering with the following approach:

1. 📝 Data Processing: Movie metadata (overview, genres, keywords, cast, crew) is combined
2. 🔤 Text Preprocessing: Stemming, lowercasing, and cleaning of text data
3. 📊 Feature Selection & Engineering : Selecting only important features removing others, creating features by merging
4. 📊 Feature Extraction: TF-IDF Vectorization converts text to numerical features
5. 📐 Similarity Calculation: Cosine similarity computed between all movies
6. 🎬 Recommendation: Top 5 most similar movies are recommended

#User Flow
Select Movie → Click Recommend → Get 5 Similar Movies

#Project Structure

Movie_Recommender_System_Deployed/
├── 📱 app.py                 # Main Streamlit application
├── 🗂️ movie_dict.pkl         # Processed movie data (LFS)
├── 🎬 movies.pkl            # Movie dataset (LFS)
├── 🔗 similarity.pkl        # Similarity matrix (LFS)
├── 📋 requirements.txt      # Project dependencies
├── 🚀 Procfile             # Deployment configuration
├── ⚙️ setup.sh             # Setup script for deployment
├── 📓 Model_Code.ipynb     # Jupyter notebook with model development
└── 📖 README.md            # Project documentation
```

#Technical Details

#Dataset
-TMDB (The Movie Database) from Kaggle

## 🎓 Learning Journey

This project represents my first step into the world of machine learning deployment. Key learnings include:

- ✅ End-to-end ML project development
- ✅ Web application development with Streamlit
- ✅ Git LFS for handling large files
- ✅ Cloud deployment and CI/CD