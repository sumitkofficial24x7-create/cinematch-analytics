import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("prepared_analysis.csv")
matrix = df.pivot_table(index='userId', columns='title', values='rating').fillna(0)
similarity_matrix = cosine_similarity(matrix.T)
similarity_df = pd.DataFrame(similarity_matrix, index=matrix.columns, columns=matrix.columns)
similarity_df.to_pickle('similarity_model.pkl')
print("✅ Brain Created.")