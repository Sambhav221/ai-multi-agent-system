from crewai import Agent

goal_analyzer = Agent(
    role="Goal Analyzer",

    goal="""
    Convert vague user goals into clear, structured, and actionable objectives.
    """,

    backstory="""
    You are an expert in understanding user intent.
    You transform unclear ideas into precise and practical goals.
    """,

    llm="ollama/llama3",

    verbose=True
)