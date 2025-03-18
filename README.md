# Simple_RAG_LLAMA
A simple RAG for LLAMA 3.2

# Project Setup

## Prerequisites

- **Docker**: Ensure Docker is installed on your system. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).
- **Ollama**: Install ollama from project's website: ollama.com

## Installation

1. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Marqo Docker container for vectordb**:

   Run the following command to start the Marqo container:

   ```bash
   docker rm -f marqo; docker run --name marqo -it -p 8882:8882 --add-host host.docker.internal:host-gateway marqoai/marqo:latest
   ```
3. **Download Llama Model**:
   Open a terminal and run the following command to download the Llama-3.2-1B-Instruct-GGUF model. You can try any other models
   supported by Ollama:
   ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
   
## Running the Project
1. **Test Data Indexing and Search by Margo Vector DB**:
   py demo/vectordb_search_demo.py
2. **Test Llama with RAG**:
   py rag_reasoning.py


