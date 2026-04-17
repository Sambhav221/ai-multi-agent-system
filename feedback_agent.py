from crewai import Agent

feedback_agent = Agent(
    role="Feedback Analyzer",

    goal="""
    Improve results based on previous outputs.
    Make outputs clearer, better structured, and more effective.
    """,

    backstory="""
    You are an expert reviewer who refines outputs and improves their quality.
    You focus on clarity, efficiency, and usefulness.
    """,

    llm="ollama/llama3",

    verbose=False
)