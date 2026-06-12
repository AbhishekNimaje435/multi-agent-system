# 🤖 Multi-Agent Research System

A powerful AI-powered Multi-Agent Research System built using LangChain, Gemini, Tavily Search, and Streamlit. The system uses multiple specialized agents to perform research, gather information from the web, and generate structured responses.

## 🚀 Live Demo

https://multi-agent-system-ld5c.onrender.com

---

## 📌 Features

* Multi-Agent Architecture
* Real-time Web Search using Tavily
* AI-Powered Research Pipeline
* Gemini LLM Integration
* Streamlit User Interface
* Modular Agent Design
* Automated Information Gathering
* Structured Research Output

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Gemini API
* Tavily Search API
* BeautifulSoup
* Requests
* Pandas

---

## 📂 Project Structure

```text
multi-agent-system/
│
├── app.py
├── agents.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/AbhishekNimaje435/multi-agent-system.git
cd multi-agent-system
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed on Render:

https://multi-agent-system-ld5c.onrender.com

---

## 🧠 How It Works

1. User enters a research query.
2. Research agents analyze the request.
3. Tavily Search retrieves relevant information.
4. Gemini processes and summarizes findings.
5. Results are presented through the Streamlit interface.

---

## 📈 Future Improvements

* Memory-enabled agents
* Multi-step reasoning workflows
* PDF report generation
* Research citations
* Vector database integration
* RAG-based knowledge retrieval

---

## 👨‍💻 Author

**Abhishek Nimaje**

GitHub:
https://github.com/AbhishekNimaje435
