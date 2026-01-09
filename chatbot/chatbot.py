print("🤖 Chatbot is online! Type 'bye' to exit.")

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! 👋"
    elif "how are you" in user_input:
        return "I'm doing great!"
    elif "your name" in user_input:
        return "I'm a Python chatbot."
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand yet."

while True:
    user = input("You: ")
    reply = get_response(user)
    print("Bot:", reply)

    if user.lower() == "bye":
        break
