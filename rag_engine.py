# rag_engine.py
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import StorageContext, load_index_from_storage

# Set up LLM and embedding model
Settings.llm = Ollama(model="gemma3:1b", request_timeout=360.0)
Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load the index from persistent storage
def get_index(persist_dir="index-persistent"):
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(storage_context)
    return index

# Query the index for a legal answer
def query_legal_index(query: str, persist_dir="index-persistent") -> str:
    index = get_index(persist_dir)
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return str(response)
