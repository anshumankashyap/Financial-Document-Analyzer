# Setup & Usage Instructions

## Prerequisites

- Python 3.8 or higher installed on your system
- `pip` available in your environment

---

## 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

---

## 2. Create a Virtual Environment
```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

> You should see `(venv)` prefixed in your terminal after activation.

---

## 4. Install `uv` (Fast Package Installer)
```bash
pip install uv
```

---

## 5. Install Dependencies from `requirements.txt`
```bash
uv pip install -r requirements.txt
```

---

## 6. Install Additional Packages
```bash
uv pip install langchain-community langchain-google-genai pypdf python-dotenv
```

| Package | Purpose |
|---|---|
| `langchain-community` | Community integrations for LangChain |
| `langchain-google-genai` | Google Generative AI (Gemini) support |
| `pypdf` | PDF reading and parsing |
| `python-dotenv` | Load environment variables from `.env` file |

---

## 7. Configure Environment Variables

Create a `.env` file in the root of your project:
```env
GOOGLE_API_KEY=AIzaSyBN_DaDfsVmXsTPq8hWHu3JhEoLCmYuApk
SERPER_API_KEY = 2a24a910e9280356f9ccd27d3347a6a7deaaf409
```

## 8. Run the Application
```bash
python main.py
```

---

## Quick Start (All Steps Combined)
```bash
python -m venv venv
venv\Scripts\activate         # Windows
# source venv/bin/activate    # macOS/Linux
pip install uv
uv pip install -r requirements.txt
uv pip install langchain-community langchain-google-genai pypdf python-dotenv
python main.py
```

## Bug Report

| # | File | Bug | Type |
|---|------|-----|------|
| 1 | `agents.py` | Wrong import: `crewai.agents` → `crewai` | Import Error |
| 2 | `agents.py` | `llm = llm` — self-reference undefined variable | **Critical** |
| 3 | `agents.py` | Agent goal instructs hallucination of advice | Design |
| 4 | `agents.py` | All backstories instruct unethical behavior | Design |
| 5 | `agents.py` | Typo: `tool=` → `tools=` | **Critical** |
| 6 | `agents.py` | `max_iter=1, max_rpm=1` makes agents non-functional | Logic |
| 7 | `agents.py` | All agents ignore their distinct roles | Design |
| 8 | `tools.py` | `from crewai_tools import tools` → `crewai.tools import tool` | Import Error |
| 9 | `tools.py` | Undefined class `Pdf()` → `PyPDFLoader()` | **Critical** |
| 10 | `tools.py` | `read_data_tool` is `async`, missing `@tool` decorator | Logic |
| 11 | `tools.py` | `InvestmentTool`/`RiskTool` are `async`, missing `@staticmethod` | Logic |
| 12 | `task.py` | All task descriptions instruct agents to fabricate data | Design |
| 13 | `task.py` | `expected_output` demands fake URLs and dangerous advice | Design |
| 14 | `task.py` | `verification` task uses `financial_analyst` instead of `verifier` | **Critical** |
| 15 | `task.py` | investment/risk tasks use wrong specialist agents | Logic |
| 16 | `main.py` | Route function name shadows imported crewAI Task | **Critical** |
| 17 | `main.py` | `query==""` SyntaxError + `reload=True` in production | Logic |

---
