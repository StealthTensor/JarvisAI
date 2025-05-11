from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
import os

# Voice assistant modules
from voice_assistant import speak, listen

# Step 1: Load documents
loader = TextLoader("data.txt")
documents = loader.load()

# Step 2: Split documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = text_splitter.split_documents(documents)

# Step 3: Create or load vector database
embedding = OllamaEmbeddings(model="nomic-embed-text")
db = Chroma.from_documents(chunks, embedding=embedding, persist_directory="db")
db.persist()

# Step 4: Setup LLM and QA chain
vectordb = Chroma(persist_directory="db", embedding_function=embedding)
retriever = vectordb.as_retriever()
llm = Ollama(model="qwen:7b")
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Step 5: Voice interaction loop
while True:
    query = listen()
    if query:
        if "exit" in query.lower() or "quit" in query.lower():
            speak("Goodbye!")
            break
        response = qa.run(query)
        speak(response)
