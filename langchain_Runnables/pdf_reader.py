from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.vectorstores import FAISS
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate

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

# Manually Retrieve Relevant Documents
query ="what is the key takeways from the document?"
retriever_docs = retriever.get_relevant_documents(query)

#combine retrieved Text into a single prompt
retrived_text = "\n".join([doc.page_content for doc in retriever_docs])

#Initialize the LLM
llm = ChatGroq( model="openai/gpt-oss-120b", temperature=0.7)

#manually Pass Retrieved Text to LLM
prompt = f"Based on the following text, answer the question: {query}\n \n{retrived_text}"
answer = llm.predict(prompt)

#Print the answer
print("Answer:", answer)