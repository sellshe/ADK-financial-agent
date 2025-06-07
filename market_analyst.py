from google.adk.agents import LlmAgent

market_analyst_agent = LlmAgent(
    name="market_analyst_agent",
    model="gemini-2.5-pro-preview-05-06",
    description="Analyzes market trends, news, earnings reports, and sentiment to assess current market conditions.",
    instruction="Gather and summarize relevant market data, earnings updates, and sector-specific trends for the given ticker.",
    output_key="market_analysis_output",
)
