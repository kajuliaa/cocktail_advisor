
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from app.memory import get_all_memories
from app.ingestion import get_cocktail_retriever

llm = OllamaLLM(model="llama3.2")
#retriever = get_combined_retriever()

template = """
You are a helpful cocktail advisor.

The user has shared the following preferences:
{user_memory}

Here are relevant cocktail knowledge snippets:
{cocktail_docs}

Here is the current user question:
{question}

Answer clearly and concisely, use provided cocktail knowledge information and user preference information.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

preference_keywords = ['favorite', 'favourite', 'like', 'love']
def is_preference_query(query):
    return any(keyword in query.lower() for keyword in preference_keywords)

def answer_query(query: str) -> str:
    

    cocktail_docs = get_cocktail_retriever().invoke(query)
    memory_docs = get_all_memories()

    cocktail_text = "\n\n".join(doc.page_content for doc in cocktail_docs)
    memory_text = "\n\n".join(memory_docs)
    if not is_preference_query(query):
        memory_text =''

    print(memory_text)
    result = chain.invoke({
        "cocktail_docs": cocktail_text,
        "user_memory": memory_text,
        "question": query
    })
    return result

