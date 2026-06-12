from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# ---------------- WRITER ----------------
writer_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert research writer. Always include URLs in Sources."),
    ("human",
     """
Topic: {topic}

Research:
{research}

Write:
- Introduction
- Key Findings (min 3)
- Conclusion
- Sources (ALL URLs)
""")
])

writer_chain = writer_prompt | llm | StrOutputParser()

# ---------------- CRITIC ----------------
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict research critic."),
    ("human",
     """
Evaluate this report:

{report}

Score: X/10
Strengths:
-
Areas to Improve:
-
Verdict:
""")
])

critic_chain = critic_prompt | llm | StrOutputParser()