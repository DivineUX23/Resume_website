from langchain import OpenAI
#from langchain.document_loaders import UnstructuredURLLoader
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
import pickle
import faiss
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass("Provide your Google API key here")


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="AIzaSyBwVvXkHRbgcp9Z2qLnDMV5lS7YfJKvIQk")


urls = [
    'https://github.com/DivineUX23/Resume/blob/main/README.md',
    'https://github.com/DivineUX23?tab=repositories',
    'https://www.linkedin.com/in/divine-igbinoba-330808184/'
]

loaders = UnstructuredURLLoader(urls=urls)
data = loaders.load()


text_splitter = CharacterTextSplitter(separator='\n', 
                                      chunk_size=1000, 
                                      chunk_overlap=200)


docs = text_splitter.split_documents(data)


#embeddings = OpenAIEmbeddings()
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")



vectorStore_openAI = FAISS.from_documents(docs, embeddings)

with open("faiss_store_openai.pkl", "wb") as f:
     pickle.dump(vectorStore_openAI, f)

with open("faiss_store_openai.pkl", "rb") as f:
    VectorStore = pickle.load(f)


#llm=OpenAI(temperature=0, model_name='')

llm=model = genai.GenerativeModel('gemini-pro')



chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=VectorStore.as_retriever())



"""
import cohere

co = cohere.Client('AlSrhcbP0GKiXYq4MoOSgzNU75bMDi7uTa0Dxqk3') # This is your trial API key

response = co.chat(
    model='command-r-plus',
    message="What year was he born?",
    temperature=0.3,
    chat_history=[
        {"role": "USER", "message": "Who discovered gravity?"},
        {
            "role": "CHATBOT",
            "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
        },
    ],
    prompt_truncation='AUTO',
    stream=True,
    connectors=[{"id":"web-search","options":{"site":"https://github.com/DivineUX23/Resume/blob/main/README.md", 
                                              "site":"https://www.linkedin.com/in/divine-igbinoba-330808184/", 
                                              "site":"https://github.com/DivineUX23?tab=repositories"}}]

)

print(response)
print(response.search_results)

"""