from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
) 


prompt1 = PromptTemplate(
    template="Generate a detail report on this {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate a 5 pointer summary of this {report}",
    input_variables=["report"]
)

parser= StrOutputParser()

chain = prompt1 | model |  parser | prompt2 | model | parser

result = chain.invoke({"topic": "unemployment in india"})

print(result)

chain.get_graph().print_ascii()