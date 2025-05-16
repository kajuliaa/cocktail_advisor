
from langchain.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

embedding = OllamaEmbeddings(model="mxbai-embed-large")
memory_db = Chroma(collection_name="memory", embedding_function=embedding, persist_directory="memory_db")

keywords = ["like", "love", 'favorite', 'favourite']

def process_memory(user_input: str):
    if any(k in user_input.lower() for k in keywords):
        memory_db.add_texts([user_input])
        return True
    return False


def get_all_memories():
    return memory_db.get()["documents"]
