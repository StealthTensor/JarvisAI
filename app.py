from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=".")

# Load model and database
embedding = OllamaEmbeddings(model="nomic-embed-text")
vectordb = Chroma(persist_directory="db", embedding_function=embedding)
retriever = vectordb.as_retriever()
llm = Ollama(model="qwen:7b")
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("message", "")
    if not query:
        return JSONResponse(content={"response": "Empty query"}, status_code=400)
    try:
        answer = qa.run(query)
        return {"response": answer}
    except Exception as e:
        return JSONResponse(content={"response": f"Error: {str(e)}"}, status_code=500)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
