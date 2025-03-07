# Simple_RAG_LLAMA
A simple RAG for LLAMA 3.2

# Project Setup

## Prerequisites

- **Docker**: Ensure Docker is installed on your system. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

## Installation

1. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Marqo Docker container**:

   Run the following command to start the Marqo container:

   ```bash
   docker rm -f marqo; docker run --name marqo -it -p 8882:8882 --add-host host.docker.internal:host-gateway marqoai/marqo:latest
   ```

## Running the Project

Once Docker and the Python dependencies are set up, you can run your project scripts as needed.