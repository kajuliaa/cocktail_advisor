import pandas as pd
from langchain.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain.retrievers import MergerRetriever
from app.memory import memory_db as mdb

cocktail_path = "data/final_cocktails.csv"
embedding = OllamaEmbeddings(model="mxbai-embed-large")
cocktail_db_path = "chroma_db"
memory_db_path = "memory_db"
cocktail_db = None
memory_db = None

def ingest():
    global cocktail_db
    df = pd.read_csv(cocktail_path)

    docs = []
    for _, row in df.iterrows():
        content = f"""
Name: {row['name']}
Alcoholic: {row['alcoholic']}
Category: {row['category']}
Glass Type: {row['glassType']}
Ingredients: {row['ingredients']}
Ingredient Measures: {row['ingredientMeasures']}
Instructions: {row['instructions']}
Thumbnail: {row['drinkThumbnail']}
Source Text: {row['text']}
"""
        docs.append(Document(page_content=content.strip()))

    cocktail_db = Chroma.from_documents(docs, embedding, persist_directory="chroma_db")


def get_cocktail_retriever():
    return Chroma(persist_directory=cocktail_db_path, embedding_function=embedding).as_retriever()
"""
def get_memory_retriever():
    return Chroma(persist_directory=memory_db_path, collection_name="memory", embedding_function=embedding).as_retriever()

def get_combined_retriever():
    global cocktail_db, memory_db
    if cocktail_db is None:
        ingest()

    
    memory_db = mdb

    retriever1 = cocktail_db.as_retriever()
    retriever2 = memory_db.as_retriever()
    return MergerRetriever(retrievers=[retriever1, retriever2])
"""