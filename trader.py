from google.adk.agents import LlmAgent

trader_agent = LlmAgent(
    name="trader_agent",
    model="gemini-2.5-pro-preview-05-06",
    description="Executes trades based on strategy and screening output. Provides entry, exit, and position size.",
    instruction=(
        "Using shortlisted stocks and risk assessment, generate a trading plan. Include entry price, stop-loss, "
        "target price, and rationale."
    ),
    output_key="trader_output",
)
