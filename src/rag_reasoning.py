import ollama
from marqo import Client

client = Client(url='http://localhost:8882')

index_name = 'simplewiki'  # Or your actual index name
reasoning_model = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

def vector_database_retrival(query, top_n=5):
    try:
        results = client.index(index_name).search(query)
        return '\n'.join([f' - {chunk['content']}' for chunk in results['hits'][:top_n]])
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

if __name__ == "__main__":
    while True:
        input_query = input("Enter your search query (or type 'exit' to quit): ")
        if input_query.lower() == 'exit':
            break

        retrieved_knowledge = vector_database_retrival(input_query)

        instruction_prompt = f'''You are a chatbot.
        Use only the following pieces of context to answer the question, 
        don't make up any new information:
        {retrieved_knowledge}
        if you think the context does not match well with the question, 
        then say that you do not know how to answer.
        '''
        print(instruction_prompt)

        stream = ollama.chat(
          model=reasoning_model,
          messages=[
            {'role': 'system', 'content': instruction_prompt},
            {'role': 'user', 'content': input_query},
          ],
          stream=True,
        )

        print('Chatbot response:')
        for chunk in stream:
          print(chunk['message']['content'], end='', flush=True)
        print('\n')