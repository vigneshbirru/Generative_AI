from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate

load_dotenv()

model1 = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
) 

#create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog  title about {topic} that will attract readers.",
)

#define the input
topic = input("Enter a topic")

#format the prompt manually using PromptTemplate
formatted_prompt = prompt.format(topic=topic)

#call the LLm direactly
blog_title = llm.predict(formatted_prompt)

#print the result
print("generated blog title:", blog_title)