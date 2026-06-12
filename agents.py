from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

from tools import web_search, scrape_url

load_dotenv()

# ---------------- MODEL ----------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# ---------------- SEARCH AGENT ----------------
def build_search_agent():
    return web_search

# ---------------- READER AGENT ----------------
def build_reader_agent():
    return scrape_url

# ---------------- WRITER ----------------
writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert research writer.

IMPORTANT:
- Use ONLY provided research
- Preserve ALL URLs exactly
- Never remove sources
- Always include Sources section with URLs
"""
    ),
    (
        "human",
        """
Write a detailed research report.

Topic: {topic}

Research:
{research}

Format:
- Introduction
- Key Findings
- Conclusion
- Sources (ALL URLs)
"""
    ),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# ---------------- CRITIC ----------------
critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a strict research critic. Be honest and precise."
    ),
    (
        "human",
        """
Evaluate this report:

{report}

Return:

Score: X/10

Strengths:
- ...

Areas to Improve:
- ...

Verdict:
...
"""
    ),
])

critic_chain = critic_prompt | llm | StrOutputParser()