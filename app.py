import pickle
import streamlit as st
import requests
import time

def fetch_poster(movie_id):
    # Temporarily disable poster fetching due to API connectivity issues
    # This prevents error messages and allows the app to work smoothly
    return None
    
    # Uncomment the code below if you want to re-enable poster fetching
    # when API connectivity is restored
    """
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            return None
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, 
            requests.exceptions.HTTPError, KeyError, Exception) as e:
        return None
    """

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        poster_url = fetch_poster(movie_id)
        recommended_movie_posters.append(poster_url)
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")

st.title('🎬 Movie Recommender System Using Machine Learning')
st.markdown("---")

# Load the pre-trained model and data
try:
    movies = pickle.load(open('artificats/movie_list.pkl','rb'))
    similarity = pickle.load(open('artificats/similary.pkl','rb'))
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {str(e)}")
    st.stop()

movie_list = movies['title'].values

st.subheader("🎯 Select a Movie")
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown:",
    movie_list,
    help="Choose any movie to get personalized recommendations"
)

st.markdown("---")

if st.button('🎬 Get Movie Recommendations', type="primary", use_container_width=True):
    with st.spinner('Getting recommendations...'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    st.success(f"Here are 5 movies similar to '{selected_movie}':")
    
    # Display movies in a vertical list
    st.markdown("### 🎬 Recommended Movies:")
    
    for i, movie_name in enumerate(recommended_movie_names, 1):
        st.markdown(f"**{i}.** {movie_name}")
    
    # Alternative: Display in a nice container format
    st.markdown("---")
    st.markdown("### 📋 Movie List:")
    
    for i, movie_name in enumerate(recommended_movie_names, 1):
        with st.container():
            st.markdown(f"""
            <div style="
                background-color: #f0f2f6; 
                padding: 10px; 
                border-radius: 5px; 
                margin: 5px 0;
                border-left: 4px solid #ff6b6b;
            ">
                <strong>{i}.</strong> {movie_name}
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
### 📊 About This System
- **Algorithm**: Content-based filtering using cosine similarity
- **Dataset**: TMDB 5000 Movies Dataset
- **Features**: Genres, keywords, cast, crew, and movie overview
- **Technology**: Python, Streamlit, scikit-learn, NLTK

### ℹ️ Note
Movie recommendations are displayed in a clean vertical list format. The recommendation engine works perfectly and shows the most similar movies based on content analysis!
""")
