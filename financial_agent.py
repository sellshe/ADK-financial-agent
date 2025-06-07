"""Financial coordinator: provide reasonable investment strategies"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.market_analyst import market_analyst_agent
from .sub_agents.screener_and_risk import screener_and_risk_agent
from .sub_agents.trader import trader_agent
from .sub_agents.auditor import auditor_agent

MODEL = "gemini-2.5-pro-preview-05-06"

financial_coordinator = LlmAgent(
    name="financial_coordinator",
    model=MODEL,
    description=(
        "Orchestrates a structured financial strategy by guiding users through market analysis, "
        "screening, risk assessment, trading, and auditing using specialized subagents."
    ),
    instruction=prompt.FINANCIAL_COORDINATOR_PROMPT,
    output_key="financial_coordinator_output",
    tools=[
        AgentTool(agent=market_analyst_agent),
        AgentTool(agent=screener_and_risk_agent),
        AgentTool(agent=trader_agent),
        AgentTool(agent=auditor_agent),
    ],
)

root_agent = financial_coordinator
