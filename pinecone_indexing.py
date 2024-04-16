# pinecone_indexing.py
from openai import OpenAI
from pinecone_ops import upsert_to_pinecone

client = OpenAI()

def get_vector_representation(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"  # You can choose an engine suitable for your needs
    )
    return response.data[0].embedding

def index_document(doc_id, text):
    vector = get_vector_representation(text)
    # Data to be indexed in Pinecone
    data = [{
        "values": vector,
        "metadata": {"text": text}  # Store original text as metadata for easy retrieval
    }]
    upsert_to_pinecone(data)
