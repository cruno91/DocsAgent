# DocsAgent
Various agentic AI examples with a vector database, RAG, chat, search, with different model interfaces.

## Prerequisites

- Python 3.13+
- Ollama

## Setup

1. [Set up an Ollama server.](https://docs.ollama.com/quickstart)
2. Add the environment variables to `.env` file.
    ```shell
   DOCSAGENT_MODEL_BACKEND=ollama
   DOCSAGENT_OLLAMA_MODEL=gpt-oss:20b
   DOCSAGENT_OLLAMA_BASE_URL=http://localhost:11434
   ```
3. Install requirements
    ```shell
   pip install -e .
   ```
4. Run the server
    ```shell
    uvicorn apps.server.main:app --reload --port 8000
    ```
   
## Usage

### API Tests

#### Hello World

```shell
curl 127.0.0.1:8000/v1/hello
```

```json
{"message":"hello world"}
```

#### LLM API

```shell
curl 127.0.0.1:8000/v1/llm-test
```

```json
{
  "backend":"configured",
  "ok":true,
  "answer":"LLM connection OK.",
  "provider":"http://localhost:11434",
  "model":"gpt-oss:20b"
}
```



```shell
curl 127.0.0.1:8000/v1/hello
```

```json
{"message":"hello world"}
```

### CLI Test

```shell
doc-agent scan-directory <directory containing pdf files> -e pdf
```

*Example:*
```shell
doc-agent scan-directory data/raw -e pdf -e md
/Users/username/data/raw/ex.md
/Users/username/data/raw/ex.pdf

doc-agent scan-directory data/raw -e pdf
/Users/username/data/raw/ex.pdf
```