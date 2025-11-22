import chromadb
from chromadb.utils import embedding_functions

# ef = embedding_functions.SentenceTransformerEmbeddingFunction(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

client = chromadb.Client()

collection_name = "ai_docs"
