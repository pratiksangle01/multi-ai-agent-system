# Multi AI Agent System 🤖🚀

> A modular, extensible Python framework that simulates how multiple AI agents collaborate in a sequential pipeline to complete complex tasks — no API key required.

---

## ✨ Features

- 🤖 Multiple specialized agents working in a coordinated pipeline
- 🔗 Sequential task execution — each agent builds on the previous output
- 🧠 Simulates real-world multi-agent AI architecture
- ⚡ Zero dependencies — pure Python, runs instantly
- 💼 Designed for automation workflows and AI prototyping
- 🧩 Modular structure — easy to extend with new agents

---

## 🧠 System Architecture

The system is built around three specialized agents that each handle a distinct role:

```
User Input
    │
    ▼
┌─────────────────┐
│  Research Agent  │  ── Analyzes the task and gathers context
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Reply Agent   │  ── Generates a professional response
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Strategy Agent  │  ── Suggests next steps and decisions
└────────┬────────┘
         │
         ▼
    Final Output
```

### 🔍 Research Agent
- Receives and analyzes the user's input task
- Extracts key context to pass downstream

### ✉️ Reply Agent
- Consumes the Research Agent's output
- Generates a structured, professional response

### 📊 Strategy Agent
- Reviews the full pipeline output
- Suggests actionable next steps and decisions

---

## 🔄 Workflow

1. User enters a task via the terminal
2. **Research Agent** processes and analyzes the task
3. **Reply Agent** generates a response based on that analysis
4. **Strategy Agent** recommends the next best action
5. The complete multi-agent output is displayed

---

## 🛠 Tech Stack

- **Language:** Python 3
- **Dependencies:** None (uses Python standard library only)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/pratiksangle01/multi-ai-agent-system.git
cd multi-ai-agent-system
```

### 2. Run the script

```bash
python agents.py
```

### 3. Enter your task when prompted.

> ✅ No API key, no installs, no configuration required.

---

## 📌 Example

**Input:**
```
Find clients for my web development service
```

**Output:**
```
[Research Agent]  Analyzing task: "Find clients for my web development service"
                  Context gathered: service type, target audience, outreach channels

[Reply Agent]     Generating response based on research...
                  Draft: "To find clients for your web dev service, focus on
                  LinkedIn outreach, freelance platforms like Upwork, and
                  building a portfolio site to showcase your work."

[Strategy Agent]  Suggested next step: Build a cold outreach list targeting
                  local SMBs and schedule 5 discovery calls this week.
```

---

## 📁 Project Structure

```
multi-ai-agent-system/
│
├── agents.py       # Main script — all agents defined here
└── README.md       # Project documentation
```

---

## 🔮 Roadmap

- [ ] Claude / GPT API integration for real AI responses
- [ ] Parallel agent execution
- [ ] Memory-based agents with session history
- [ ] Autonomous decision-making loop
- [ ] REST API wrapper for external integration
- [ ] Web dashboard interface

---

## 🧩 Extensions & Ideas

- Connect agents to a database for persistent memory
- Plug in external APIs (news, CRM, email) per agent
- Add a Manager Agent to coordinate and delegate tasks
- Export agent outputs to a structured report or CSV

---

## 💼 Use Cases

- AI automation system prototyping
- Business workflow automation
- Client communication pipelines
- Learning and experimenting with agent-based architecture

---

## 👨‍💻 Author

**Pratik Sangle**  
Feel free to connect, open an issue, or contribute!

---

⭐ If this project helped you, consider giving it a star — it means a lot!
