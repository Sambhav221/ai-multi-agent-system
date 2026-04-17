from crewai import Agent

executor = Agent(
    role="Executor",

    goal="""
    Execute tasks step by step efficiently and produce practical outputs.
    Generate real-world results like plans, reports, and drafts.
    """,

    backstory="""
    You are a highly skilled execution specialist who turns ideas into reality.
    You focus on delivering clear, actionable, and usable outputs.
    """,

    llm="ollama/llama3",

    verbose=True
)