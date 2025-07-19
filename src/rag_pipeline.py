# src/rag_pipeline.py
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load vector index and metadata
index = faiss.read_index("vector_store/faiss_index.index")

with open("vector_store/documents.pkl", "rb") as f:
    documents = pickle.load(f)

with open("vector_store/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_chunks(question, k=5):
    """Embed question and retrieve top-k relevant chunks."""
    question_embedding = model.encode([question])
    _, indices = index.search(np.array(question_embedding), k)
    results = [documents[i] for i in indices[0]]
    result_meta = [metadata[i] for i in indices[0]]
    return results, result_meta
