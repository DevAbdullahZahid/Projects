from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import groq

import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
# Debugging: Check if the API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in the .env file.")
openai.api_key = api_key
print(f"API Key: {openai.api_key}")




web_search_agent = Agent(
    name="Web search agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)


Financial_agent =Agent(
    name="Financial Agent",
    role="Search for the Best Stocks",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True)
        ],
    instructions=["Include Tables to Show the Data"],
    show_tools_calls=True,
    markdown=True,
)


multi_model_ai_Agent = Agent(
    model=Groq(id="llama-3.1-70b-versatile"),
    team=[web_search_agent,Financial_agent],
    instructions=["Always include sources","Use table and graphs to diaplay the data"],
    show_tool_calls=True,
    markdown=True,
)


multi_model_ai_Agent.print_response("Summarize analyst reccommendation and share the latest news of NVDA",stream=True)