## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import tool            # @tool decorator lives in crewai, NOT crewai_tools
from crewai_tools import SerperDevTool   # SerperDevTool is in crewai_tools
from langchain_community.document_loaders import PyPDFLoader

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
class FinancialDocumentTool():
    @staticmethod
    @tool("Read Financial Document")
    def read_data_tool(path: str = 'data/sample.pdf') -> str:
        """Tool to read data from a pdf file from a path.

        Args:
            path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

        Returns:
            str: Full Financial Document file content
        """

        docs = PyPDFLoader(file_path=path).load()

        full_report = ""
        for data in docs:
            # Clean and format the financial document data
            content = data.page_content

            # Remove extra whitespaces and format properly
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")

            full_report += content + "\n"

        return full_report

## Creating Investment Analysis Tool
class InvestmentTool:
    @staticmethod
    def analyze_investment_tool(financial_document_data: str) -> str:
        # Process and analyze the financial document data
        processed_data = financial_document_data

        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1

        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    @staticmethod
    def create_risk_assessment_tool(financial_document_data: str) -> str:
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented"