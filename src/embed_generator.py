from sentence_transformers import SentenceTransformer
import pandas as pd

# Load the model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Load the data
df = pd.read_csv('/Users/praveenkumarkumaresan/code/mlops_homework5/data/6000_all_categories_questions.csv')  # Adjust path if needed

# Generate embeddings using the 'prompt' column
df['embedding'] = df['prompt'].apply(lambda x: model.encode(x).tolist())

# Save embeddings
df.to_pickle('/Users/praveenkumarkumaresan/code/mlops_homework5/data/embeddings.pkl')
