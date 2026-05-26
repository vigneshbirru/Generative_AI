from huggingface_hub import InferenceClient

client = InferenceClient(
    model="google/flan-t5-large",
    HF_TOKEN = os.getenv("HF_TOKEN")
)

print(client.text_generation("What is Hugging Face?"))