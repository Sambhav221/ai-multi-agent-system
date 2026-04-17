# 🤖 AI Multi-Agent System

A powerful **Multi-Agent AI System** built using **CrewAI, Ollama, and Streamlit** that can understand a user’s goal, break it into steps, execute it, and refine the output.

---

## 🚀 Features

- 🧠 Multi-Agent Architecture (Planner, Executor, Reviewer)
- ⚡ Local LLM using Ollama (No API cost)
- 🌐 Streamlit Web Interface
- 📄 Generates real-world outputs:
  - Study Plans
  - Business Plans
  - Email Drafts
  - Strategies
- 📥 Download output as file
- 🔁 Retry & session memory support

---

## 🏗️ Architecture

---

## 🛠️ Tech Stack

- **Python**
- **CrewAI**
- **Ollama (LLaMA3)**
- **Streamlit**
- **Git & GitHub**

---

## 📂 Project Structure

Mini AutoGPT/
│
├── app.py # Streamlit UI
├── main.py # Core AI logic
│
├── agents/
│ ├── planner.py
│ ├── executor.py
│ ├── reviewer.py
│
├── tools/ # (Optional tools)
│
├── .gitignore
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-multi-agent-system.git
cd ai-multi-agent-system

2 - *Create virtual environment*
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ How to Operate
Run :- ollama run llama3
After that , Run:- streamlit run app.py


Example Use Cases

Try inputs like:-
Create a 7-day study plan for Operating Systems
Generate a startup idea and business plan
