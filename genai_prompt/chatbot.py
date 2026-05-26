from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1
)

chat_history = [SystemMessage(content="You are a helpful assistant")]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)
    
print(chat_history)