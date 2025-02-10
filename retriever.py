from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import os

# Initialize Chroma DB client
client = chromadb.Client()
collection = client.create_collection("askdoc")

# Load Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to split text into chunks
def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks

# Function to add documents to Chroma DB
def add_document_to_chroma(doc_id, text):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks)

    # Store in Chroma DB
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            ids=[f"{doc_id}_{i}"],
            documents=[chunk],
            embeddings=[embedding.tolist()]
        )
    print(f"Document {doc_id} added to Chroma DB.")

# Function to retrieve relevant chunks based on query
def retrieve_relevant_chunks(query, top_k=3):
    query_embedding = model.encode([query])[0]
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    retrieved_chunks = [doc for doc in results['documents'][0]]
    return retrieved_chunks

# Example usage
if __name__ == "__main__":
    sample_text = """Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn. It includes areas like machine learning, natural language processing, robotics, and more."""
    add_document_to_chroma("doc1", sample_text)

    query = "What is AI?"
    relevant_chunks = retrieve_relevant_chunks(query)
    print("Relevant Chunks:", relevant_chunks)
