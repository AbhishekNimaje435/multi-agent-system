from tools import web_search, scrape_url
from agents import writer_chain, critic_chain

def run_research_pipeline(topic: str):

    state = {}

    # ---------------- STEP 1: SEARCH ----------------
    search_results = web_search.invoke({"query": topic})
    state["search"] = search_results

    # ---------------- STEP 2: SCRAPE ----------------
    first_url = None

    for line in search_results.split("\n"):
        if "URL:" in line:
            first_url = line.replace("URL:", "").strip()
            break

    scraped_text = ""

    if first_url:
        scraped_text = scrape_url.invoke({"url": first_url})
    else:
        scraped_text = "No URL found to scrape."

    state["scraped"] = scraped_text

    # ---------------- STEP 3: WRITE ----------------
    research = f"""
SEARCH RESULTS:
{search_results}

SCRAPED CONTENT:
{scraped_text}
"""

    report = writer_chain.invoke({
        "topic": topic,
        "research": research
    })

    state["report"] = report

    # ---------------- STEP 4: CRITIC ----------------
    feedback = critic_chain.invoke({
        "report": report
    })

    state["feedback"] = feedback

    return state