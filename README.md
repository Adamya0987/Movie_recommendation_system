# 🎬 Movie Recommendation System

A machine learning-powered movie recommendation system that suggests similar movies based on content analysis. Built with Python, Streamlit, and scikit-learn, this system uses content-based filtering to provide personalized movie recommendations.

## 🌟 Features

- **Content-Based Filtering**: Recommends movies based on similar content (genres, cast, crew, keywords, overview)
- **Interactive Web Interface**: Beautiful Streamlit-based web application
- **Real-time Recommendations**: Get instant movie suggestions with just one click
- **Comprehensive Dataset**: Built on TMDB 5000 movies dataset with detailed metadata

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.herokuapp.com)

## 📊 Dataset

The system uses the **TMDB 5000 Movies Dataset** which includes:
- **tmdb_5000_movies.csv**: Movie metadata (title, overview, genres, keywords, budget, revenue, etc.)
- **tmdb_5000_credits.csv**: Cast and crew information for each movie

### Dataset Features:
- 5000+ movies with comprehensive metadata
- Movie genres, keywords, and plot summaries
- Cast and crew information
- Budget, revenue, and popularity metrics
- Production companies and countries

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Text Processing**: NLTK (Porter Stemmer)
- **Similarity Algorithm**: Cosine Similarity
- **API Integration**: The Movie Database (TMDB) API
- **Deployment**: Heroku (with Procfile)

## 📁 Project Structure

```
movie-recommendation-project/
├── app.py                          # Main Streamlit application
├── Recommender system.ipynb        # Jupyter notebook for model development
├── tmdb_5000_movies.csv           # Movies dataset
├── tmdb_5000_credits.csv          # Credits dataset
├── artificats/                    # Pre-trained model artifacts
│   ├── movie_list.pkl            # Processed movie data
│   └── similary.pkl              # Similarity matrix
├── requirement.txt                # Python dependencies
├── setup.py                      # Package setup configuration
├── setup.sh                      # Heroku deployment script
├── Procfile                      # Heroku process configuration
└── README.md                     # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/movie-recommendation-project.git
   cd movie-recommendation-project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:8501`

### Dependencies

The project requires the following Python packages:
- `streamlit` - Web application framework
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `scikit-learn` - Machine learning library
- `nltk` - Natural language processing
- `requests` - HTTP library for API calls
- `pickle` - Object serialization

## 🎯 How It Works

### 1. Data Preprocessing
- **Data Merging**: Combines movies and credits datasets
- **Feature Extraction**: Extracts genres, keywords, cast, crew, and overview
- **Text Processing**: 
  - Converts JSON strings to lists
  - Removes spaces from text
  - Applies Porter stemming for better text matching
- **Tag Creation**: Combines all features into a single tag string

### 2. Machine Learning Pipeline
- **Vectorization**: Uses CountVectorizer to convert text to numerical vectors
- **Similarity Calculation**: Computes cosine similarity between all movie pairs
- **Model Persistence**: Saves processed data and similarity matrix using pickle

### 3. Recommendation Engine
- **Content-Based Filtering**: Finds movies with similar content features
- **Similarity Ranking**: Ranks movies by similarity score
- **Top-K Selection**: Returns top 5 most similar movies

### 4. Web Interface
- **Movie Selection**: Dropdown with all available movies
- **Recommendation Display**: Shows 5 recommended movies with posters
- **API Integration**: Fetches movie posters from TMDB API

## 🎮 Usage

1. **Select a Movie**: Choose any movie from the dropdown menu
2. **Get Recommendations**: Click "Show Recommendation" button
3. **View Results**: See 5 similar movies with their posters and titles

### Example Recommendations

If you select **"The Dark Knight Rises"**, the system might recommend:
- Batman Begins
- The Dark Knight
- Inception
- Interstellar
- Dunkirk

## 🚀 Deployment

### Heroku Deployment

The project is configured for Heroku deployment:

1. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

2. **Deploy**
   ```bash
   git push heroku main
   ```

3. **Open App**
   ```bash
   heroku open
   ```

### Environment Variables

For production deployment, consider setting these environment variables:
- `TMDB_API_KEY`: Your TMDB API key (currently hardcoded)

## 🔍 Model Performance

The recommendation system uses:
- **Algorithm**: Content-based filtering with cosine similarity
- **Features**: Genres, keywords, cast, crew, and movie overview
- **Vectorization**: TF-IDF with 5000 most frequent features
- **Similarity Metric**: Cosine similarity for robust recommendations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Adamya Jain**
- Email: adamya0987@gmail.com
- GitHub: [@your-username](https://github.com/your-username)

## 🙏 Acknowledgments

- [The Movie Database (TMDB)](https://www.themoviedb.org/) for providing the dataset and API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [scikit-learn](https://scikit-learn.org/) for machine learning tools
- [Heroku](https://www.heroku.com/) for deployment platform

## 📊 Dataset Source

The dataset used in this project is the **TMDB 5000 Movie Dataset** available on Kaggle:
- [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

## 🔮 Future Enhancements

- [ ] User-based collaborative filtering
- [ ] Hybrid recommendation system
- [ ] User rating and feedback system
- [ ] Movie trailer integration
- [ ] Advanced filtering options (year, rating, language)
- [ ] Recommendation explanation feature
- [ ] Mobile-responsive design improvements

---

⭐ **Star this repository if you found it helpful!**

