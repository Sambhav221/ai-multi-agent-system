from crewai.tools import tool

@tool
def search_web(query: str) -> str:
    """Mock web search (fast version)"""
    return f"Search results for: {query}"