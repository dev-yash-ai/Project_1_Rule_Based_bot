def run_chatbot():
    # 1. The Knowledge Base
    responses = {
        "project 1": "Project 1 is the foundation phase: The Rule-Based AI Chatbot. It focuses on Control Flow and explicit logic.",
        "goal": "The goal is to create a continuous digital loop that simulates basic human interaction.",
        "probabilistic": "System 1: The Artist. This refers to AI that generates outputs based on probability (like LLMs).",
        "deterministic": "System 2: The Engineer. This is what I am. I provide exact, hard-coded outputs.",
        "white box": "A transparent program where we can always explain exactly how an output was generated.",
        "guardrails": "Deterministic filters placed around probabilistic LLMs to ensure safety and blocking.",
        "ipo model": "The foundational blueprint consisting of Input, Process, and Output.",
        "infinite loop": "The continuous cycle that acts as my heartbeat, keeping me alive until a kill command is received.",
        "hash map": "A dictionary data structure that provides instant lookup time.",
    }

    # 2. The Initialization & Menu Phase
    print("--- DecodeLabs Rule-Based AI Chatbot ---")
    print("Welcome! Here are the specific terms you can ask me about:\n")

    # This automatically prints every keyword from our dictionary as a menu
    for keyword in responses.keys():
        print(f" - {keyword}")

    print("\nPlease type a keyword exactly as shown above.")
    print("If you are not interested, type 'exit' to leave. Have a nice day!\n")

    # 3. The Continuous Loop
    while True:
        raw_text = input("User: ")
        clean_text = raw_text.lower().strip()

        # Exit Strategy
        if clean_text == "exit":
            print("System: Shutting down. Have a nice day!")
            break

        # Intent Matching & Fallback
        reply = responses.get(clean_text, "System: I don't know about this. Please pick a word from the list.")
        print(f"Bot: {reply}\n")


# Run the program
if __name__ == "__main__":
    run_chatbot()