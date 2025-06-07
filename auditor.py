from google.adk.agents import LlmAgent

auditor_agent = LlmAgent(
    name="auditor_agent",
    model="gemini-2.5-pro-preview-05-06",
    description="Audits the overall financial strategy. Evaluates allocation efficiency, trade performance, and offers suggestions.",
    instruction="Review the portfolio allocation and past trades. Suggest changes to optimize return and minimize risk.",
    output_key="audit_output",
)
