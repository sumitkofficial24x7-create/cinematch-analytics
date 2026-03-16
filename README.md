# 🎬 Cinematch Analytics

### Movie Recommendation System + Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)\
![Machine
Learning](https://img.shields.io/badge/Machine%20Learning-Recommendation%20System-green)\
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)\
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

Cinematch Analytics is an end-to-end data science project that builds a
movie recommendation system and analytics dashboard from scratch.

The system analyzes user rating behavior from the MovieLens Dataset and
recommends movies using item‑based collaborative filtering with Cosine
Similarity.

The final product is an interactive web application powered by Streamlit
where users can:

• Get movie recommendations\
• Explore analytics insights\
• Understand rating trends and genre popularity

------------------------------------------------------------------------

# 🚀 Project Highlights

✔ Built a movie recommendation engine\
✔ Processed 100k+ movie ratings\
✔ Implemented collaborative filtering\
✔ Created interactive analytics dashboard\
✔ Delivered a complete end-to-end ML project

------------------------------------------------------------------------

# 📂 Project Structure

    Cinematch-Analytics/

    data/
     ├── raw/
     │   ├── movies.csv
     │   ├── ratings.csv
     │   ├── tags.csv
     │   ├── links.csv
     │
     ├── processed/
     │   ├── analysis.csv
     │   └── prepared_analysis.csv

    notebooks/
     ├── 01_data_cleaning.ipynb
     ├── 02_data_preparation.ipynb
     ├── 03_testing.ipynb

    app.py
    main.py
    trainer.py
    similarity_model.pkl
    prepared_analysis.csv

------------------------------------------------------------------------

# 📊 Dataset

Dataset used: MovieLens Dataset

Dataset scale:

• 100,836 ratings\
• 9,700+ movies\
• 600+ users

Important columns include:

userId -- Unique user identifier\
movieId -- Unique movie identifier\
rating -- User rating\
timestamp -- Rating time\
title -- Movie title\
genres -- Movie genres\
year -- Movie release year\
average_rating -- Average movie rating\
num_ratings -- Number of ratings

------------------------------------------------------------------------

# 🧹 Step 1 --- Data Cleaning

Raw files:

• movies.csv\
• ratings.csv\
• tags.csv\
• links.csv

Using Python and pandas:

• Merged movie and rating datasets\
• Removed duplicates\
• Handled missing values\
• Converted timestamps\
• Extracted movie release year

Output dataset:

analysis.csv

------------------------------------------------------------------------

# 🔧 Step 2 --- Data Preparation

Created additional features:

• average_rating\
• num_ratings

Filtered movies with very low rating counts.

Final dataset:

prepared_analysis.csv

------------------------------------------------------------------------

# 🧠 Step 3 --- User--Movie Matrix

Structure:

Rows → Users\
Columns → Movies\
Values → Ratings

Missing ratings replaced with 0.

------------------------------------------------------------------------

# 🤖 Step 4 --- Collaborative Filtering

Implemented item‑based collaborative filtering.

Cosine Similarity used to measure similarity between movie rating
vectors.

Model stored as:

similarity_model.pkl

------------------------------------------------------------------------

# 🎥 Step 5 --- Recommendation Engine

System workflow:

1.  Accept movie title\
2.  Find similarity scores\
3.  Sort results\
4.  Return top 10 similar movies

Example:

Input: Toy Story

Recommendations:

Toy Story 2\
Monsters Inc\
Finding Nemo\
Shrek

------------------------------------------------------------------------

# 📈 Step 6 --- Analytics Dashboard

Dashboard built with Streamlit.

Charts include:

• Rating distribution\
• Top popular movies\
• Highest rated movies\
• Genre popularity\
• Rating vs popularity scatter plot\
• Movie release trends

Visualization libraries:

Matplotlib\
Seaborn\
Plotly

------------------------------------------------------------------------

# 💻 Run the Application

Clone the repository:

git clone https://github.com/sumitkofficial24x7-create/cinematch-analytics.git

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

------------------------------------------------------------------------

# 🛠 Technologies Used

Python\
Pandas\
NumPy\
Scikit-learn\
Streamlit\
Matplotlib\
Seaborn\
Plotly

------------------------------------------------------------------------

# 🎯 Future Improvements Possible

• Add movie posters using TMDB API\
• Hybrid recommendation system\
• Real-time data integration\
• Cloud deployment\
• Personalized user recommendations

------------------------------------------------------------------------

# ⭐ Final Outcome

Cinematch Analytics demonstrates:

✔ Data cleaning and preprocessing\
✔ Machine learning recommendation systems\
✔ Interactive dashboards\
✔ End-to-end data science workflow

If you found this project useful, consider starring the repository on
GitHub.
