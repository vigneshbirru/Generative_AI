from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv  
from langchain_core.runnables import RunnableSequence , RunnableLambda, RunnableParallel, RunnablePassthrough, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate.from_template(
    "write a detail report on {topic}"
)
prompt2 = PromptTemplate.from_template(
    "Summary the following text {topic}"
)


model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
) 

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>200, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({"topic": "AI"})

print(result)