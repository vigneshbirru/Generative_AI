from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence 

load_dotenv()

prompt = PromptTemplate.from_template(
    "write a answer the following \n {question} from the  following text -\n{text}"
)
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
) 

parser = StrOutputParser()

url ='https://vaibhav-bhoir.netlify.app/'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({"question": "What is this website about?", "text": docs[0].page_content})   )