import sys
import os
from dotenv import load_dotenv

# 🔥 Fix import path (Streamlit safe)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Load environment
load_dotenv()

from crewai import Task, Crew

# ✅ Only essential agents (PERMANENT FIX)
from agents.planner import planner
from agents.executor import executor
from agents.reviewer import reviewer


def run_ai_system(goal: str) -> str:
    """
    Runs optimized AI multi-agent system (FAST + STABLE)
    """

    # Input validation
    if not goal or goal.strip() == "":
        return "⚠️ Please enter a valid goal."

    try:
        # -------------------------------
        # Task 1: Planning
        # -------------------------------
        plan_task = Task(
            description=f"""
            Break this goal into clear and simple steps:
            {goal}

            Keep it short, structured, and actionable.
            """,
            expected_output="Step-by-step plan",
            agent=planner
        )

        # -------------------------------
        # Task 2: Execution
        # -------------------------------
        execute_task = Task(
            description="""
            Execute the plan and generate practical real-world output.

            Examples:
            - Study plan
            - Business plan
            - Email draft
            - Strategy

            Keep output clear and usable.
            """,
            expected_output="Final execution output",
            agent=executor
        )

        # -------------------------------
        # Task 3: Review
        # -------------------------------
        review_task = Task(
            description="""
            Improve and polish the output:
            - Fix clarity
            - Improve structure
            - Make it professional
            """,
            expected_output="Final polished output",
            agent=reviewer
        )

        # -------------------------------
        # Crew Setup (FAST)
        # -------------------------------
        crew = Crew(
            agents=[planner, executor, reviewer],
            tasks=[plan_task, execute_task, review_task],
            verbose=False   # ⚡ Faster
        )

        result = crew.kickoff()

        return str(result)

    except Exception as e:
        return f"❌ System Error:\n{str(e)}"