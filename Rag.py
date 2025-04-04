import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from duckduckgo_search import DDGS  # Import DuckDuckGo search

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def search_duckduckgo(query):
    """Fetch web search results using DuckDuckGo."""
    try:
        with DDGS() as ddgs:
            results = [r["body"] for r in ddgs.text(query, max_results=1)]
            return "\n".join(results)
    except Exception as e:
        return None


def setup_rag_chain(url):
    """
    Loads data, creates embeddings, vector store, and the RAG chain for a given URL.
    Returns the retriever for later use.
    """
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        if not docs:
            return None

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = text_splitter.split_documents(docs)

        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_store = FAISS.from_documents(split_docs, embeddings)

        return vector_store.as_retriever(search_kwargs={'k': 5})
    except Exception as e:
        return None