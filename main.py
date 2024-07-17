from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchainget.query import query,get_conversational_chain
import os
from db.db import connect_to_mongo

class QueryRequest(BaseModel):
    prompt: str

app = FastAPI()
collection = connect_to_mongo()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class content(BaseModel):
    text: str

@app.post("/storevector")
async def storevector(text: content):
    with open("db\Coding Ninjas.txt", "a") as file:
        file.write(text.text)
    file.close()
    file = open("db\Coding Ninjas.txt")
    cont = file.read()

    loader = TextLoader("db\Coding Ninjas.txt")
    docs = loader.load()
    text_spiliter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=20)
    splits = text_spiliter.split_documents(docs)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=os.getenv('GEMINI_API_KEY'))
    store = [] 
    embedding = []
    for split in splits:
        store.append(split.page_content)
    
    docsearch = MongoDBAtlasVectorSearch.from_documents(splits, embeddings, collection=collection, index_name="embeddings")
    
    #return docsearch
    return "Embeddings saved to MongoDB vector base"

@app.post("/queryresult")
async def queryResult(request: QueryRequest):
    getdocs = query(collection,request.prompt)
    chain = get_conversational_chain()
    response = chain(
        {"input_documents":getdocs,"question": request.prompt},
        return_only_outputs=True
        )
    
    return {"result":response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)