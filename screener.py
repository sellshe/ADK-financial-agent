from google.adk.agents import LlmAgent

screener_and_risk_agent = LlmAgent(
    name="screener_and_risk_agent",
    model="gemini-2.5-pro-preview-05-06",
    description="Screens stocks based on indicators like RSI, volume, growth, and assesses associated risks.",
    instruction=(
        "Use technical and fundamental indicators (RSI, volume, moving averages, financial ratios) "
        "to shortlist stocks. Evaluate risk using volatility, beta, and sector sensitivity."
    ),
    output_key="screening_risk_output",
)
