from langchain_community.document_loaders import PyPDFLoader
Pdfloader = PyPDFLoader("GenAI Syllabus-deatail.pdf")
doc = Pdfloader.load()

print("len",len(doc))
print("page content",doc[0].page_content)
print("meta data",doc[0].metadata)