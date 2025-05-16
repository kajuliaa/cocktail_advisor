from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.rag import answer_query
from app.memory import process_memory

app = FastAPI()
templates = Jinja2Templates(directory='app/templates')

chat_history =[]

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chat_history": chat_history})

@app.post("/chat", response_class=HTMLResponse)
def chat(request: Request, user_input: str = Form(...)):
    memory_note = process_memory(user_input)
    response = answer_query(user_input)
    chat_history.append(("User", user_input))
    chat_history.append(("Bot", response))
    return templates.TemplateResponse("index.html", {"request": request, "chat_history": chat_history})