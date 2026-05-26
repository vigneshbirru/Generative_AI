from langchain_huggingface import HuggingFaceEmbeddings

embedding  = HuggingFaceEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2')


document = [
    "delhi is the capital of india",
    "paris is the capital of france",
    "kolkata is the capital of west bengal"
]

text ="delhi is the capital of india"

vector = embedding.embed_query(text)    

print(str(vector))