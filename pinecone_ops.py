# pinecone_ops.py
import os
from pinecone import Pinecone, ServerlessSpec
from config import PINECONE_API_KEY, PINECONE_INDEX_NAME

# Initialize Pinecone
api_key = PINECONE_API_KEY  
index_name = PINECONE_INDEX_NAME
pc = Pinecone(api_key=api_key)

# Function to check and create an index if it doesn't exist
def initialize_index(index_name, dimension=1536, metric='cosine'):
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric=metric,
            spec=ServerlessSpec(cloud='aws', region='us-west-2')
        )
    print(f"Index {index_name} is ready.")

# Upsert data into Pinecone
def upsert_to_pinecone(index_name, data):
    index = pc.Index(name=index_name)
    index.upsert(vectors=data)  # Corrected the structure here
    print(f"Data upserted successfully into {index_name}.")

# Query Pinecone
def query_pinecone(query_vector, top_k=5):
    index = pc.Index(name=index_name)
    print('Query Vector:\n\n', query_vector)
    print(query_vector)
    return index.query(query_vector=query_vector, top_k=top_k)
