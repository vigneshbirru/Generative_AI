from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence 

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
) 
prompt = PromptTemplate.from_template(
    "write a summary for the following poem: -\n{poem}"
)

parser = StrOutputParser()

loader = TextLoader("example.txt",encoding="utf-8")

doc = loader.load()

print("type",type(doc))

print("len",len(doc))

print("[]",doc[0])

chain = prompt | model | parser

print(chain.invoke({"poem": doc[0].page_content}))