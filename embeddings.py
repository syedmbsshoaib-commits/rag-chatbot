from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def chunk_text(text, chunk_size=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def find_relevant_chunks(query, chunks, top_k=2):
    vectorizer = TfidfVectorizer()
    all_texts = chunks + [query]
    matrix = vectorizer.fit_transform(all_texts)
    chunk_vecs = matrix[:-1]
    query_vec = matrix[-1]
    scores = cosine_similarity(query_vec, chunk_vecs)[0]
    top_indices = np.argsort(scores)[-top_k:][::-1]
    return [chunks[i] for i in top_indices]