from agents import build_reader_agent, writer_chain, critic_chain
from tools import web_search


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # STEP 1 - WEB SEARCH
    print("\n" + "=" * 50)
    print("STEP 1 - Web Search Tool is working...")
    print("=" * 50)

    search_results = web_search.invoke({
        "query": topic
    })

    state["search_results"] = search_results

    print("\nSearch Results:\n")
    print(state["search_results"])

    # STEP 2 - READER AGENT
    print("\n" + "=" * 50)
    print("STEP 2 - Reader Agent is scraping top resources...")
    print("=" * 50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [(
            "user",
            f"""
Based on the following search results about '{topic}':

1. Extract the most relevant URL.
2. Use the scrape_url tool.
3. Return the scraped content.

Search Results:

{state["search_results"]}
"""
        )]
    })

    state["scraped_content"] = reader_result["messages"][-1].content

    print("\nScraped Content:\n")
    print(state["scraped_content"])

    # STEP 3 - WRITER
    print("\n" + "=" * 50)
    print("STEP 3 - Writer is drafting the report...")
    print("=" * 50)

    research_combined = f"""
SEARCH RESULTS

{state["search_results"]}

DETAILED SCRAPED CONTENT

{state["scraped_content"]}
"""

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nFINAL REPORT\n")
    print(state["report"])

    # STEP 4 - CRITIC
    print("\n" + "=" * 50)
    print("STEP 4 - Critic is reviewing the report...")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCRITIC FEEDBACK\n")
    print(state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\nEnter a research topic: ")

    result = run_research_pipeline(topic)

    print("\n" + "=" * 50)
    print("FINAL REPORT")
    print("=" * 50)
    print(result["report"])

    print("\n" + "=" * 50)
    print("CRITIC FEEDBACK")
    print("=" * 50)
    print(result["feedback"])