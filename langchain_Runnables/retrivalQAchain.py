from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.vectorstores import FAISS
from dotenv import load_dotenv  
from langchain.chains import RetrievalQA

#load the document
loader = TextLoader("docs.txt")
documents = loader.load()

#split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

#convert text into embeddings & store in FAISS
vectorstore = FAISS.from_documents(docs, ChatGroq.embeddings())

#create a retriever (fetches relevant documents based on a query)
retriever = vectorstore.as_retriever()

#Initialize the LLM
llm = ChatGroq( model="openai/gpt-oss-120b", temperature=0.7)

#create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Manually Retrieve Relevant Documents
query ="what is the key takeways from the document?"
answer = qa_chain.run(query)


print("Answer:", answer)