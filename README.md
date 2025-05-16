# 🍹 Cocktail Advisor Chat 

### Thought Process & Key Decisions

- **Cocktails Information**: All relevant fields from the cocktail dataset are used using `Chroma` with `mxbai-embed-large` embeddings. 

- **User Preferences**: User preferences prompt is identified with following words `like`, `love`, `favourite`. A separate Chroma collection `memory_db` is used to store user preferences. Preferences info is passed only if prompt contains `preferences_keywords`

### Results

- The system answers questions about cocktails based on provided data.
- It also considers user preferences and stores them for future use.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/cocktail-advisor.git
cd cocktail-advisor
```

---

## Environment Setup

### Option A: Using Conda 
```bash
conda create -n cocktail-rag python=3.10
conda activate cocktail-rag
pip install -r requirements.txt
```

### Option B: Using venv
```bash
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows
pip install -r requirements.txt
```

---

## LLM & Embedding Models

### 1. Install Ollama

Follow the instructions:  
https://ollama.com/download

### 2. Download the Required Models
```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

---

## ▶ Start the App

```bash
uvicorn app.main:app --reload
```

Then open in your browser:  
[http://localhost:8000](http://localhost:8000)

### Files 

- **`main.py`**: FastAPI application routes the user input from the web form to processing logic and renders the HTML chat template.
- **`ingestion.py`**: Reads cocktail dataset CSV, converts each row into a structured document, and stores it in Chroma using embedding.
- **`rag.py`**: Builds the prompt for the LLM using LangChain, combining cocktail info and user memory only when needed, and calls the model to generate a reply.
- **`memory.py`**: Monitors user input for preference keywords and saves them to a separate memory DB. Also exposes helper functions to retrieve memory.
- **`index.html`**: A web interface.
- **`final_cocktails.csv`**: Contains all cocktail metadata used for document ingestion and retrieval.
- **`chroma_db/`** and **`memory_db/`**: Automatically generated folders that store vector embeddings and metadata for cocktail and user preferences.
