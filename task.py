## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description=(
        "Analyze the financial document located at 'data/sample.pdf' to answer the user's query: {query}\n"
        "Steps:\n"
        "1. Use the read_data_tool to extract the full content of the financial document.\n"
        "2. Carefully read and interpret the financial data including revenues, profits, cash flows, and key metrics.\n"
        "3. Identify relevant sections of the document that directly address the user's query.\n"
        "4. Use web search only to supplement with verified market context if necessary.\n"
        "5. Provide a structured, evidence-based analysis with specific figures cited from the document."
    ),
    expected_output=(
        "A well-structured financial analysis report that:\n"
        "- Directly answers the user's query with data from the document\n"
        "- Includes specific financial figures, ratios, and metrics cited from the report\n"
        "- Provides clear sections: Summary, Key Financial Highlights, Analysis, and Conclusion\n"
        "- Uses accurate financial terminology\n"
        "- Cites only real, verifiable sources\n"
        "- Is formatted in clear markdown"
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description=(
        "Based on the financial document at 'data/sample.pdf', conduct an investment analysis for the query: {query}\n"
        "Steps:\n"
        "1. Read the financial document using read_data_tool.\n"
        "2. Analyze key investment indicators: revenue trends, profit margins, EPS, cash flow, debt levels.\n"
        "3. Compare current performance against prior periods using data in the document.\n"
        "4. Identify growth drivers and risks mentioned in the document.\n"
        "5. Provide data-backed investment insights."
    ),
    expected_output=(
        "A concise investment analysis that:\n"
        "- Summarizes financial performance with specific numbers\n"
        "- Identifies key investment strengths and concerns based on the data\n"
        "- Provides a balanced view of opportunities and risks\n"
        "- Recommends further due diligence areas\n"
        "- Does NOT make specific buy/sell recommendations without sufficient data"
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description=(
        "Perform a risk assessment based on the financial document at 'data/sample.pdf' for query: {query}\n"
        "Steps:\n"
        "1. Read the financial document using read_data_tool.\n"
        "2. Identify financial risk factors: liquidity risk, market risk, operational risk, and credit risk.\n"
        "3. Analyze financial ratios relevant to risk: debt-to-equity, current ratio, interest coverage, etc.\n"
        "4. Review any risk disclosures or forward-looking statements in the document.\n"
        "5. Provide a balanced risk assessment with mitigation suggestions."
    ),
    expected_output=(
        "A structured risk assessment report that:\n"
        "- Identifies specific risks with supporting evidence from the document\n"
        "- Quantifies risks using actual financial figures where possible\n"
        "- Categorizes risks by type (financial, operational, market, regulatory)\n"
        "- Suggests practical risk mitigation strategies\n"
        "- Provides a clear overall risk rating with justification"
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

verification = Task(
    description=(
        "Verify that the uploaded file at 'data/sample.pdf' is a legitimate financial document.\n"
        "Steps:\n"
        "1. Read the document using read_data_tool.\n"
        "2. Check for the presence of standard financial report components: financial statements, "
        "revenue figures, expense breakdowns, or other quantitative financial data.\n"
        "3. Confirm the document's authenticity and relevance to financial analysis.\n"
        "4. Report any issues, missing sections, or anomalies found."
    ),
    expected_output=(
        "A verification report that:\n"
        "- Confirms whether the document is a valid financial report (Yes/No with reasoning)\n"
        "- Lists the financial components found (e.g., income statement, balance sheet, cash flow)\n"
        "- Notes the reporting period and entity name if identifiable\n"
        "- Flags any missing standard sections or data quality concerns\n"
        "- Provides the actual file path verified"
    ),
    agent=verifier,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)
