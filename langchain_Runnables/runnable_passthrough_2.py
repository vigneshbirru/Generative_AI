from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel

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

joke_generation_chain = RunnableSequence(prompt, model, parser)
parallel_chain =  RunnableParallel({
        "Generate_joke": RunnablePassthrough(),
        "Explain_joke": RunnableSequence(prompt2, model, parser)
    })

final_chain = RunnableSequence(joke_generation_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

print("generate joke:", result['Generate_joke'])
print("explain joke:", result['Explain_joke'])
