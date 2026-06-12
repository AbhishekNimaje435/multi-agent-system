import streamlit as st
import time
from pipeline import run_research_pipeline

st.set_page_config(page_title="AI Research Agent", layout="wide")

st.title("🔬 AI Research Agent")

topic = st.text_input("Enter topic")

if st.button("Run Pipeline"):

    if not topic.strip():
        st.warning("Enter topic first")

    else:
        with st.spinner("Running research pipeline..."):

            result = run_research_pipeline(topic)

        st.subheader("🔍 Search Results")
        st.write(result["search"])

        st.subheader("📄 Scraped Content")
        st.write(result["scraped"])

        st.subheader("📝 Final Report")
        st.write(result["report"])

        st.subheader("🧐 Critic Feedback")
        st.write(result["feedback"])

        st.success("Done!")