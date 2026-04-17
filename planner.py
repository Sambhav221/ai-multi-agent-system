from crewai import Agent

planner = Agent(
    role="Planner",
    goal="Break goals into clear, short steps",
    backstory="You are an expert in simplifying complex tasks",
    llm="ollama/llama3:8b",
    verbose=False
)