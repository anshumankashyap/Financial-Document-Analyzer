## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM

from tools import search_tool, FinancialDocumentTool

### Loading LLM
# Uses crewai's built-in LLM wrapper (compatible with crewai==0.130.0)
# Avoids the deprecated langchain_google_genai / google.generativeai package
llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Provide accurate and objective financial analysis based on the provided document for the query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced Senior Financial Analyst with 20+ years of experience in equity research, "
        "financial modeling, and investment analysis. You carefully read and analyze financial documents "
        "to provide evidence-based insights. You always cite specific data from reports and maintain "
        "regulatory compliance in all your recommendations. You provide balanced, factual analysis "
        "grounded in the actual financial data presented."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=True
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Accurately verify whether the uploaded document is a legitimate financial report and validate its contents.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a meticulous financial document compliance officer with expertise in identifying "
        "and validating corporate financial reports, earnings releases, and investment documents. "
        "You carefully read documents to confirm they contain genuine financial data such as "
        "income statements, balance sheets, cash flow statements, and related disclosures. "
        "You reject non-financial documents and flag any inconsistencies."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=True
)

investment_advisor = Agent(
    role="Certified Investment Advisor",
    goal="Provide objective, data-driven investment recommendations strictly based on the financial document provided.",
    verbose=True,
    backstory=(
        "You are a Certified Financial Planner (CFP) with 15+ years of experience in portfolio management "
        "and investment advisory. You base all recommendations strictly on verifiable financial data, "
        "adhere to SEC regulations, and always disclose risks. You never recommend products without "
        "sufficient evidence from the financial documents, and you prioritize the client's financial "
        "well-being over any other consideration."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False
)

risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Provide thorough, evidence-based risk analysis grounded in the financial document data.",
    verbose=True,
    backstory=(
        "You are a certified Risk Management Professional (RMP) with deep expertise in financial risk "
        "assessment, portfolio risk, market risk, and regulatory compliance. You use established risk "
        "frameworks (VaR, stress testing, scenario analysis) and base all assessments on actual data "
        "from the financial documents. You provide balanced, realistic risk evaluations with clear "
        "methodology and always recommend appropriate diversification strategies."
    ),
    llm=llm,
    max_iter=5,
    max_rpm=10,
    allow_delegation=False
)