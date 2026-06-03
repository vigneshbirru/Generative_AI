from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence , RunnableLambda, RunnableParallel, RunnablePassthrough

load_dotenv()

def word_count(text):
    return len(text.split())

prompt = PromptTemplate.from_template(
    "write a joke about {topic}"
)
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
) 

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)


parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)
