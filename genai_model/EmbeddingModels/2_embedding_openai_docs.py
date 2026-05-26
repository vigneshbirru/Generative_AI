from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding  = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32)

document = [
    "delhi is the capital of india",
    "paris is the capital of france",
    "kolkata is the capital of west bengal"
]

result = embedding.embed_documents(document)
print(str(result))