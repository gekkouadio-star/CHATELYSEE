import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

def initialiser_chatelysee(api_key):
    # 1. Charger les documents du dossier 'data'
    loader = DirectoryLoader('./data/', glob="./*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()

    # 2. Créer une base de données "cerveau" (Vector Store)
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = Chroma.from_documents(docs, embeddings)

    # 3. Configurer le modèle de réponse
    llm = ChatOpenAI(model_name="gpt-4", temperature=0, openai_api_key=api_key)
    
    # 4. Créer la chaîne de question-réponse
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever())
    return qa_chain