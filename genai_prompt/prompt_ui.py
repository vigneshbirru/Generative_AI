from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=1
)

st.header("Research Tool") 

    
paper_input = st.selectbox("Select a research paper", ["Attention Is All You Need", 
                                                    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
                                                    "GPT-3: Language Models are Few-Shot Learners",
                                                    "Diffusion Models Beat GANs on Image Synthesis"])    

style_input = st.selectbox("select Explanation Style", ["Beginner-Friendly", "Technical",
                                                        "Code-Oriented", "Mathematical" ])
    
length_input = st.selectbox("Select Explanation Length", ["Short (1-2 sentences)", "Medium (1-2 paragraphs)", "Long (Detailed explanation)"])    
    

    
    
#template
    
template = load_prompt("template.json") 
#fill the placeholder


if st.button("Summarize"):
    chain = template | model
    response = chain.invoke({ 
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input}) 
    
    st.write(response.content)
