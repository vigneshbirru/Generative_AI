from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence 

load_dotenv()

prompt = PromptTemplate.from_template(
    "write a joke about {topic}"
)
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
) 

parser = StrOutputParser()

prompt2 = PromptTemplate.from_template(
    "Explain the following joke: {text}"

)
chain = RunnableSequence(prompt, model, parser,prompt2, model, parser)


result = chain.invoke({"topic": "AI"})

print(result)
