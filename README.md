# 🍹 Cocktail Advisor Chat 


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
