from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
df = pd.read_pickle('/Users/praveenkumarkumaresan/code/mlops_homework5/data/embeddings.pkl')

def retrieve_similar_excerpts(query, top_k=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, df['embedding'].tolist())[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    return df.iloc[top_indices][['prompt']]  # If needed, rename 'prompt' to 'excerpt' in DataFrame