from crewai import Agent

reviewer = Agent(
    role="Reviewer",
    goal="Improve and finalize output with clarity",
    backstory="You refine outputs into high-quality results",
    llm="ollama/llama3:8b",
    verbose=False
)