import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load embedding model once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def load_reference_chunks(folder_path):
    """
    Loads and chunks text files from a folder.

    Args:
        folder_path (str): Path to folder containing reference .txt files.

    Returns:
        List[str]: List of text chunks.
    """
    chunks = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip non-text files
        if not filename.lower().endswith(".txt"):
            continue

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

            # Simple chunking: split every 500 characters
            chunk_size = 500
            for i in range(0, len(text), chunk_size):
                chunk = text[i:i + chunk_size].strip()
                if chunk:
                    chunks.append(chunk)

        except Exception as e:
            print(f"Error reading {filename}: {e}")

    return chunks

def build_faiss_index(chunks):
    """
    Builds a FAISS index from text chunks.

    Args:
        chunks (List[str]): List of text chunks.

    Returns:
        faiss.IndexFlatL2, np.ndarray, List[str]: FAISS index, embeddings, and original chunks.
    """
    embeddings = embedding_model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, embeddings, chunks

def retrieve_relevant_chunks(query, index, chunks, top_k=5):
    """
    Retrieves top-k relevant chunks for a query.

    Args:
        query (str): User query.
        index (faiss.IndexFlatL2): FAISS index.
        chunks (List[str]): Original text chunks.
        top_k (int): Number of results to return.

    Returns:
        List[str]: Top-k relevant chunks.
    """
    query_embedding = embedding_model.encode([query])
    _, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]
