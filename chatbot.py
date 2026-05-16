# Rule-Based AI Chatbot
# DecodeLabs Industrial Training | Batch 2026
# Developer: Mayar Yasser

# VERSION 1: if-else approach (Basic)

def get_response_ifelse(user_input):
    if user_input == 'hello' or user_input == 'hi':
        return 'Hi there! I am Maya, your AI Assistant!'
    elif user_input == 'how are you':
        return "I'm fully operational and ready to assist!"
    elif user_input == 'what is ai':
        return 'AI is when machines think and learn like humans!'
    elif user_input == 'what is a chatbot':
        return 'A chatbot is a program that simulates human conversation!'
    elif user_input == 'what can you do':
        return 'I can answer your questions using rule-based logic!'
    elif user_input == 'bye':
        return 'Goodbye! Keep learning and building 🚀'
    elif user_input == 'help':
        return 'Try asking: what is ai, who made you, or tell me a joke!'
    else:
        return "I don't understand that yet. Try asking something else!"


# VERSION 2: Dictionary approach (Upgraded)

def get_response_dict(user_input):
    responses = {
        # Greetings
        'hello': 'Hi there! I am Maya, your AI Assistant!',
        'hi': 'Hey! Maya here, how can I help you?',
        'how are you': "I'm fully operational and ready to assist!",

        # About the Bot
        'what is your name': 'My name is Maya!',
        'who made you': 'I was built by Mayar Yasser at DecodeLabs Batch 2026!',
        'are you human': 'Nope! I am a rule-based AI chatbot 🤖',

        # About DecodeLabs
        'what is decodelabs': 'DecodeLabs helps students and young professionals build career-ready skills through practical, mentor-guided virtual internship.',

        # AI Questions
        'what is ai': 'AI is when machines think and learn like humans!',
        'what is a chatbot': 'A chatbot is a program that simulates human conversation!',
        'what can you do': 'I can answer your questions using rule-based logic!',

        # Fun
        'tell me a joke': 'Why do programmers prefer dark mode? Because light attracts bugs! 🐛',
        'motivate me': 'Every expert was once a beginner. Keep coding Mayar! 💪',

        # Goodbye
        'bye': 'Goodbye! Keep learning and building 🚀',
        'help': 'Try asking: what is ai, who made you, or tell me a joke!'
    }
    return responses.get(user_input, "I don't understand that yet. Try asking something else!")


# MAIN LOOP

def main():
    print("=" * 40)
    print("   DecodeLabs AI Chatbot - Project 1")
    print("=" * 40)
    print("Type 'exit' to quit.\n")

    while True:
        raw_input_text = input("You: ")
        clean_input = raw_input_text.lower().strip()

        if clean_input == 'exit':
            print("Bot: Goodbye! See you next time.")
            break

        response = get_response_dict(clean_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()