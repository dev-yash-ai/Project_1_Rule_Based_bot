# Rule-Based AI Chatbot (Project 1)

## Overview
This project is a deterministic, rule-based AI chatbot built as the foundation phase of the DecodeLabs Industrial Training. It serves as a "white box" system, providing exact, hard-coded outputs without the hallucination risks associated with probabilistic Large Language Models (LLMs).

## Architecture
The system is built using the **IPO (Input, Process, Output) Model**:
*   **Input & Sanitization:** Captures user text and normalizes it (lowercasing and stripping whitespace) to ensure predictable data processing.
*   **Process (Logic Engine):** Bypasses inefficient `if-elif` ladders by utilizing a Hash Map (Python Dictionary) for instant $O(1)$ lookup time.
*   **Output (Feedback Loop):** Returns mapped intents or a secure fallback response using the atomic `.get()` method. 
*   **Heartbeat:** The entire system runs inside an infinite `while` loop until explicitly terminated by a kill command.

## How to Run
1. Run `main.py` in your terminal or IDE.
2. Select a keyword from the initial menu.
3. Type `exit` to shut down the system.

## Technologies Used
*   Python 3.x
*   Control Flow & Decision-making logic
