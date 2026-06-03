from langchain_community.document_loaders import UnstructuredPDFLoader

# Path of PDF file
pdf_path = "pdf1.pdf"

# Create Loader
loader = UnstructuredPDFLoader(pdf_path)

# Load PDF
documents = loader.load()

# Print Information
print(f"Total Pages/Chunks: {len(documents)}")

for i, doc in enumerate(documents[:3]):
    print(f"\n--- Document {i+1} ---")
    print("Metadata:", doc.metadata)
    print("Content:")
    print(doc.page_content[:500])