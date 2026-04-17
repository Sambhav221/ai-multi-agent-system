import sys
import os

# 🔥 Ensure project root is in path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st
from main import run_ai_system

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Multi-Agent System",
    page_icon="🤖",
    layout="centered"
)

# -------------------------------
# Session State
# -------------------------------
if "result" not in st.session_state:
    st.session_state.result = None

if "goal" not in st.session_state:
    st.session_state.goal = ""

# -------------------------------
# Header UI
# -------------------------------
st.title("🤖 AI Multi-Agent System")
st.markdown("### Enter your goal and let AI agents handle everything 🚀")

# -------------------------------
# Input
# -------------------------------
goal = st.text_input("Enter your goal:", value=st.session_state.goal)

# -------------------------------
# Buttons
# -------------------------------
col1, col2 = st.columns(2)

run_clicked = col1.button("🚀 Run System", use_container_width=True)
retry_clicked = col2.button("🔁 Retry", use_container_width=True)

# -------------------------------
# Execution Logic
# -------------------------------
if run_clicked or retry_clicked:

    if not goal.strip():
        st.warning("⚠️ Please enter a goal")
    else:
        st.session_state.goal = goal

        with st.spinner("🤖 Agents are thinking... (30–60 sec)"):
            try:
                result = run_ai_system(goal)
                st.session_state.result = result
                st.success("✅ Completed!")

            except Exception as e:
                st.error("❌ Error occurred:")
                st.code(str(e))

# -------------------------------
# Output Section
# -------------------------------
if st.session_state.result:

    st.divider()
    st.subheader("🔥 Final Output")

    # Better formatting
    st.markdown(st.session_state.result)

    # -------------------------------
    # Action Buttons
    # -------------------------------
    col1, col2, col3 = st.columns(3)

    # Download
    col1.download_button(
        label="📥 Download",
        data=str(st.session_state.result),
        file_name="ai_output.txt",
        mime="text/plain",
        use_container_width=True
    )

    # Copy (real copy using text area)
    with col2:
        st.text_area("📋 Copy Output", st.session_state.result, height=100)

    # Clear
    if col3.button("🧹 Clear", use_container_width=True):
        st.session_state.result = None
        st.session_state.goal = ""
        st.rerun()

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("🚀 Built with CrewAI + Ollama + Streamlit")