import streamlit as st
import time
from pipeline import run_research_pipeline

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ResearchMind",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #050816;
    color: white;
    font-family: 'Arial';
}

/* Remove default streamlit spacing */
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* Title */
.big-title {
    font-size: 90px;
    font-weight: 900;
    color: white;
    margin-bottom: 0;
}

.orange {
    color: #ff8c2a;
}

/* Subtitle */
.subtitle {
    font-size: 22px;
    color: #a0a0a0;
    margin-bottom: 40px;
}

/* Pipeline cards */
.card {
    background: #0f1724;
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 18px;
    border: 1px solid #1f2937;
}

.card-title {
    font-size: 24px;
    font-weight: bold;
    color: white;
}

.waiting {
    float:right;
    color: gray;
    font-size:14px;
}

/* Input box */
.stTextInput input {
    background: #111827;
    color: white;
    border-radius: 12px;
    border: 1px solid #374151;
    height: 50px;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg,#ff7b00,#ff9e42);
    color: black;
    font-weight: bold;
    border: none;
    border-radius: 14px;
    height: 55px;
    font-size: 18px;
}

.stButton > button:hover {
    background: #ff8c2a;
}

.result-box {
    background:#0f1724;
    padding:20px;
    border-radius:15px;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
left, right = st.columns([1.3, 1])

# ---------------- LEFT SIDE ----------------
with left:
    st.markdown(
        '<div class="big-title">Research<span class="orange">Mind</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Four specialized AI agents collaborate — searching, scraping, writing, and critiquing.</div>',
        unsafe_allow_html=True
    )

    topic = st.text_input("", placeholder="Quantum computing breakthroughs in 2025")

    run = st.button("⚡ Run Research Pipeline")

# ---------------- RIGHT SIDE ----------------
with right:

    st.markdown("""
    <div class="card">
        <div class="card-title">01 Search Agent <span class="waiting">WAITING</span></div>
        <p>Gathers recent web information</p>
    </div>

    <div class="card">
        <div class="card-title">02 Reader Agent <span class="waiting">WAITING</span></div>
        <p>Scrapes & extracts deep content</p>
    </div>

    <div class="card">
        <div class="card-title">03 Writer Chain <span class="waiting">WAITING</span></div>
        <p>Drafts the full research report</p>
    </div>

    <div class="card">
        <div class="card-title">04 Critic Chain <span class="waiting">WAITING</span></div>
        <p>Reviews quality and improves output</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- PIPELINE ----------------
if run:

    if not topic.strip():
        st.warning("Please enter topic")

    else:

        progress = st.progress(0, "Running AI Agents...")

        try:
            progress.progress(20, "Search Agent Running...")
            time.sleep(1)

            progress.progress(40, "Reader Agent Running...")
            time.sleep(1)

            progress.progress(60, "Writer Agent Running...")
            time.sleep(1)

            progress.progress(80, "Critic Agent Running...")
            time.sleep(1)

            result = run_research_pipeline(topic)

            progress.progress(100, "Done")

            st.success("Research Completed")

            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("🔍 Search Results")
            st.write(result.get("search", ""))
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("📄 Scraped Content")
            st.write(result.get("scraped", ""))
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("📝 Final Report")
            st.markdown(result.get("report", ""))
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("🧐 Critic Feedback")
            st.markdown(result.get("feedback", ""))
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(str(e))