
from langchain_groq import ChatGroq
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
) 


parser = JsonOutputParser()

# 1st prompt -> detailed report
template = PromptTemplate(
    template = "Give me the name , age and city of a fictional person \n {format_instructions}",
    input_variables=["format_instructions"],
    partial_variables={"format_instructions": parser.get_format_instructions() }
)

# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template | model | parser
final_result = chain.invoke({})
print(final_result['name'])
print(type(final_result))