import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain_groq import ChatGroq
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

def query(collection, query):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=os.getenv("GOOGLE_API_KEY"))
    vectorStore = MongoDBAtlasVectorSearch(collection, embeddings, index_name="vector_index")
    try:
        print("inside the function")
        print(query)
        docs = vectorStore.similarity_search(query, K=4)
        print("Vector Search Results:")
        print(len(docs))
        return docs
    except Exception as e:
        print("Database timeout or error:", str(e))


def get_conversational_chain():
    prompt_template = """
    Answer the question as a chatbot, the answer should not be too short, nor should it be too long, the answer should be 50 to 75 words long,
    if the answer is not in provided context just say, "I'm sorry, I cannot answer this question right now", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGroq(model = "llama-3.1-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain