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
