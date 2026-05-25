## Two Approaches Used

### Approach 1: if-else (Basic)
The straightforward way — checks each condition one by one.
- Complexity: O(n) — gets slower as rules increase

### Approach 2: Dictionary (Upgraded) ✅
Uses a hash map for instant lookup regardless of rules count.
- Complexity: O(1) — always instant

> Both approaches are implemented in chatbot.py
> The main loop uses the Dictionary approach for better performance.