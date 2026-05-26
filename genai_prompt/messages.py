from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv 
load_dotenv()
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1,
    token_limit=10
) 

messages = [
    SystemMessage(content="you are a helpful assistant "),
    HumanMessage(content="Tell me about langchain"),  
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)