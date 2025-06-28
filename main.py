import streamlit as st
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize the agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="Engineered to assist First, Second, Third, and Final year engineering students of all branches. Delivers high-quality, exam-ready answers in a structured format add detailed theory as per exam: Definition ➤ Explanation ➤ Diagram (if required) ➤ Example ➤ Applications. Perfect for theory-based university exams like SPPU. Designed to boost marks and clarity with every response",
    tools=[DuckDuckGoTools()],
    markdown=True
)

st.set_page_config(page_title="AI Analyst Chat Assistant", layout="wide")
st.title("AI Analyst Chat Assistant")
st.write("""
Ask any engineering theory question and get a detailed, exam-ready answer!
""")

user_input = st.text_area("Enter your question:", "What is data science? Tell me its advantages, uses, and future.")

if st.button("Get Answer"):
    with st.spinner("Generating answer..."):
        response = agent.get_response(user_input)
        st.markdown(response)
