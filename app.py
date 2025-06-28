
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


agent=Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="Engineered to assist First, Second, Third, and Final year engineering students of all branches. Delivers high-quality, exam-ready answers in a structured format add detailed theory as per exam: Definition ➤ Explanation ➤ Diagram (if required) ➤ Example ➤ Applications. Perfect for theory-based university exams like SPPU. Designed to boost marks and clarity with every response",
    tools=[DuckDuckGoTools()],
    markdown=True
)

#agent.print_response("What is a linked list? Explain types with example diagrams.")
##agent.print_response("What is a circular queue? Explain with example diagrams with pros and cons.")
agent.print_response("what is the data science tell me its advantages and its uses as well as future.")

