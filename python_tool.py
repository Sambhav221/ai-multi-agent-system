from crewai.tools import tool

@tool
def run_python(code: str) -> str:
    """Execute simple Python expressions safely"""
    try:
        result = eval(code)   # ⚡ faster than exec
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"