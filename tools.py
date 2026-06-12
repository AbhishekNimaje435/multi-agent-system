from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# ---------------- WEB SEARCH ----------------
@tool
def web_search(query: str) -> str:
    """Search web and return titles, URLs, snippets"""
    results = tavily.search(query=query, max_results=5)

    output = []
    for r in results["results"]:
        output.append(
            f"TITLE: {r['title']}\nURL: {r['url']}\nSNIPPET: {r['content'][:300]}"
        )

    return "\n\n---\n\n".join(output)

# ---------------- SCRAPER ----------------
@tool
def scrape_url(url: str) -> str:
    """Scrape webpage content"""
    try:
        res = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(separator=" ", strip=True)[:3000]

    except Exception as e:
        return f"Scraping failed: {str(e)}"
