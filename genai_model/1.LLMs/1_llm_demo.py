from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of India?"
        }
    ],
    temperature=0.9
)

# Equivalent to print(results)
print(completion.choices[0].message.content)