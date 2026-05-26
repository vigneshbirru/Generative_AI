from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
) 

schema = [
    ResponseSchema(name='fact_1', description="fact 1 about the topic"),
    ResponseSchema(name='fact_2', description="fact 2 about the topic"),
    ResponseSchema(name='fact_3', description="fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give exactly 3 facts about {topic} in JSON format.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({"topic": "black hole"})
print(result)