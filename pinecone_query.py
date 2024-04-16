from pinecone_ops import query_pinecone
from pinecone_indexing import get_vector_representation

def search_for_process_descriptions(process_names):
    results = {}
    for name in process_names:
        query_vector = get_vector_representation(name)
        print(query_vector)
        search_results = query_pinecone(query_vector, top_k=1)  # Retrieve the most relevant document for each process
        if search_results:
            results[name] = search_results[0]['metadata']['text']  # Store the text of the most relevant document
        else:
            results[name] = "No relevant documentation found."
    return results

def search_for_process(description):
    query_vector = get_vector_representation(description)
    results = query_pinecone(query_vector, top_k=1)  # Retrieve the most relevant document
    if results:
        return results[0]['metadata']['text']  # Return the text of the most relevant document
    else:
        return "No relevant documentation found."