from marqo import Client

client = Client(url='http://localhost:8882')

index_name = 'simplewiki'  # Or your actual index name

def search_vector_database(query):
    try:
        results = client.index(index_name).search(query)
        print(f"Search results for query '{query}':")
        for hit in results['hits']:
            print(f"  - Score: {hit['_score']}, Title: {hit['title']}, hightlights: {hit['_highlights']}, Content Snippet: {hit['content'][:200]}...") # Truncate content for brevity
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        query = input("Enter your search query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        search_vector_database(query)