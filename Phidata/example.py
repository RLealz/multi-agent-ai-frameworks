from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

finance_agent = Agent(
    name="Finance AI Agent",
    model=OpenAIChat(id="gpt-4"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True)],
    instructions=["Use tables to display data"],
)

finance_agent.print_response("Summarize analyst recommendations for TSLA", stream=True)