import openai
from phi.agent import   Agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq

import os 
import phi 
from phi.playground import Playground, serve_playground_app
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")



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



app=Playground(agents=[Financial_agent,web_search_agent]).get_app()


if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)