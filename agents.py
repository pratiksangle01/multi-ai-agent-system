def research_agent(task):
    return f"[Research Agent] Analyzing task: {task}"

def reply_agent(data):
    return f"[Reply Agent] Creating response based on: {data}"

def strategy_agent(reply):
    return f"[Strategy Agent] Suggested next step after: {reply}"

def main():
    print("=== Multi AI Agent System ===\n")
    
    task = input("Enter your task:\n")
    
    research = research_agent(task)
    reply = reply_agent(research)
    strategy = strategy_agent(reply)
    
    print("\n--- OUTPUT ---\n")
    print(research)
    print(reply)
    print(strategy)

if __name__ == "__main__":
    main()
