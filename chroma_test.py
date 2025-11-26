import chromadb
import sys

try:
    # The HttpClient is used to connect to a remote Chroma server
    client = chromadb.HttpClient(host='http://localhost:8000')
    
    # Create or get a collection
    collection = client.get_or_create_collection("test_collection")
    
    # Add documents to the collection
    collection.add(
        documents=["This is a document about Cline", "This is a document about AI assistants"],
        metadatas=[{"source": "cline"}, {"source": "ai"}],
        ids=["id1", "id2"]
    )
    
    # Query the collection
    results = collection.query(
        query_texts=["What is Cline?"],
        n_results=1
    )
    
    print("Query results:")
    print(results)

except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)
    sys.exit(1)
