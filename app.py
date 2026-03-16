import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Configuration
st.set_page_config(
    page_title="CineMatch AI & Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Styling (Updated for Dashboard)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #1a1c24;
        border-radius: 10px 10px 0px 0px; color: white; padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #FF4B4B; }
    .stButton>button {
        width: 100%; border-radius: 20px; background: linear-gradient(45deg, #FF4B4B, #FF8E53);
        color: white; border: none; height: 3em; font-weight: bold;
    }
    .movie-card {
        background-color: #1a1c24; padding: 20px; border-radius: 15px; border: 1px solid #333;
        text-align: center; height: 160px; display: flex; flex-direction: column;
        justify-content: center; transition: transform 0.3s;
    }
    .movie-card:hover { transform: scale(1.05); border-color: #FF4B4B; }
    </style>
    """, unsafe_allow_html=True)


# 3. Data Loading
@st.cache_resource
def load_data():
    sim_df = pd.read_pickle('similarity_model.pkl')
    full_df = pd.read_csv('prepared_analysis.csv')
    return sim_df, full_df


movie_similarity_df, full_df = load_data()

# --- APP LAYOUT (TABS) ---
tab_rec, tab_dash = st.tabs(["🎯 Recommendations", "📊 Insights Dashboard"])

# --- TAB 1: RECOMMENDATIONS ---
with tab_rec:
    st.title("🎬 CineMatch AI")
    st.markdown("##### *Advanced Recommendation Engine v2.6*")

    col1, col2 = st.columns([3, 1])
    with col1:
        selected_movie = st.selectbox(
            "Type a movie you loved:", movie_similarity_df.columns.values,
            index=None, placeholder="Search 5,000+ Titles..."
        )
    with col2:
        st.write("##")
        run_button = st.button("Generate Picks")

    if run_button and selected_movie:
        recommendations = movie_similarity_df[selected_movie].sort_values(ascending=False).iloc[1:11]

        # Grid Layout
        for row in range(2):
            cols = st.columns(5)
            for i in range(5):
                idx = i + (row * 5)
                with cols[i]:
                    title = recommendations.index[idx]
                    score = recommendations.values[idx]
                    st.markdown(f"""
                        <div class="movie-card">
                            <p style='font-size: 14px; font-weight: bold;'>{title}</p>
                            <p style='color: #FF4B4B; font-size: 12px;'>{int(score * 100)}% Match</p>
                        </div>
                        """, unsafe_allow_html=True)
            st.write("#")
    else:
        st.info("Pick a movie above to initialize the neural recommendation engine.")

# --- TAB 2: ANALYTICS DASHBOARD ---
with tab_dash:
    st.title("📈 Platform Analytics")
    st.write("Real-time insights into user behavior and movie trends.")

    # Top Row: Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Ratings", len(full_df))
    m2.metric("Movies in Catalog", full_df['title'].nunique())
    m3.metric("Avg Community Rating", f"{full_df['rating'].mean():.2f} ★")
    m4.metric("Active Users", full_df['userId'].nunique())

    st.markdown("---")

    # Second Row: Distribution & Popularity
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Rating Distribution")
        fig_hist = px.histogram(full_df, x="rating", nbins=10,
                                color_discrete_sequence=['#FF4B4B'], template="plotly_dark")
        st.plotly_chart(fig_hist, use_container_width=True)

    with c2:
        st.subheader("Top 10 Most Rated Movies")
        pop_data = full_df.groupby('title')['num_ratings'].max().sort_values(ascending=False).head(10)
        fig_bar = px.bar(pop_data, x=pop_data.values, y=pop_data.index, orientation='h',
                         color=pop_data.values, color_continuous_scale='Reds', template="plotly_dark")
        st.plotly_chart(fig_bar, use_container_width=True)

    # Third Row: Quality vs Popularity
    st.subheader("The 'Hidden Gems' Scatter Plot")
    # Grouping to ensure one dot per movie
    scatter_data = full_df.groupby('title').agg({'average_rating': 'mean', 'num_ratings': 'max'}).reset_index()
    fig_scatter = px.scatter(scatter_data, x="num_ratings", y="average_rating",
                             hover_name="title", color="average_rating",
                             color_continuous_scale='Plasma', template="plotly_dark",
                             labels={"num_ratings": "Popularity (Votes)", "average_rating": "Quality (Rating)"})
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Fourth Row: Genre & Trends
    c3, c4 = st.columns(2)
    with c3:
        st.subheader("Genre Popularity")
        genre_counts = full_df['genres'].str.get_dummies(sep='|').sum().sort_values(ascending=False).head(10)
        fig_pie = px.pie(values=genre_counts.values, names=genre_counts.index, hole=0.4,
                         color_discrete_sequence=px.colors.sequential.RdBu, template="plotly_dark")
        st.plotly_chart(fig_pie, use_container_width=True)

    with c4:
        st.subheader("Movie Release Trends")
        year_trends = full_df.groupby('year')['title'].nunique()
        fig_line = px.line(x=year_trends.index, y=year_trends.values,
                           line_shape="spline", template="plotly_dark")
        fig_line.update_traces(line_color='#FF4B4B')
        st.plotly_chart(fig_line, use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2026 CineMatch AI | Advanced Portfolio Project")