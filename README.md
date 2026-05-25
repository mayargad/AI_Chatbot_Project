# Rule-Based AI Chatbot 🤖

> Project 1 | DecodeLabs Industrial Training | Batch 2026
> Developer: Mayar Yasser

## Overview
A rule-based chatbot built with pure Python logic.
Uses a dictionary-based knowledge base for O(1) response lookup.

## Two Approaches Used

### Approach 1: if-else (Basic)
The straightforward way — checks each condition one by one.
- Complexity: O(n) — gets slower as rules increase

### Approach 2: Dictionary (Upgraded) ✅
Uses a hash map for instant lookup regardless of rules count.
- Complexity: O(1) — always instant

## Features
- Continuous input loop (while True)
- Input sanitization (lowercase + strip)
- Dictionary-based knowledge base (8+ intents)
- Fallback response for unknown inputs
- Clean exit command
- Custom bot personality (Maya)

## How to Run
```bash
python chatbot.py
```

## Example

You: hello
Bot: Hi there! I am Maya, your AI Assistant!
You: what is ai
Bot: AI is when machines think and learn like humans!
You: exit
Bot: Goodbye! See you next time.


## Concepts Used
- Control Flow & Decision Making
- Hash Maps / Dictionaries (O(1) lookup)
- Input Sanitization
- IPO Model (Input → Process → Output)

## Tools Used
- Python

## Developer
Mayar Yasser | DecodeLabs Batch 2026