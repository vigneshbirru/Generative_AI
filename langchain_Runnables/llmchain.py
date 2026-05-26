from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

#Load the LLM (GPT-OSS-120B)
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)

#Create a Prompt Template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="suggest a catchy blog title about {topic}."
)

#Create an LLM Chain
chain = LLMChain(llm=llm, prompt=prompt_template)


# Run the chain with an specfic topic
topic = "LoRA & QLoRA fine-tuning techniques"
blog_title = chain.run(topic)

print("Generated Blog Title:", blog_title)