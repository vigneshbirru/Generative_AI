from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence ,RunnableParallel

load_dotenv()

prompt = PromptTemplate.from_template(
    "Generate  a tweet about {topic}"
)
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
) 

parser = StrOutputParser()

prompt2 = PromptTemplate.from_template(
    "generate a LinkedIn post about {topic}"

)
paraellel_chain = RunnableParallel( {
    'tweet': RunnableSequence(prompt, model, parser),
    'linkedin_post': RunnableSequence(prompt2, model, parser)
})


parallel_result = paraellel_chain.invoke({"topic": "AI"})

print("tweet:", parallel_result['tweet'])
print("LinkedIn post:", parallel_result['linkedin_post'])