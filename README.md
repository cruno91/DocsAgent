# DocsAgent
Various agentic AI examples with a vector database, RAG, chat, search, with different model interfaces.

## Setup

1. Install requirements
    ```shell
   pip install -e .
   ```
2. Run the server
    ```shell
    uvicorn apps.server.main:app --reload --port 8000
    ```
   
## Usage

### API Test

```shell
curl 127.0.0.1:8000/v1/api
```

```json
{"message":"hello world"}
```