from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Replace with your target URL
url = "https://github.com/facebookresearch/faiss/blob/main/INSTALL.md"

loader = WebBaseLoader(url)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)  # Use 'chunks' instead of overwriting 'documents'
embeddings = OllamaEmbeddings(model="llama2")  # Change model name if needed

vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")

query = input("input query: ")
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
results = retriever.get_relevant_documents(query)