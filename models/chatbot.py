class Chatbot:
    def __init__(self):
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! How are you feeling?",
            "Hey! I'm here to listen. What's on your mind?"
        ]

    def respond(self, message):
        message = message.strip().lower()
        if any(greet in message for greet in ["hello", "hi", "hey"]):
            return self.greetings[0]
        elif "sad" in message or "unhappy" in message:
            return "I'm sorry you're feeling that way. Would you like to talk more about it?"
        elif "help" in message or "support" in message:
            return "I'm here to support you. Can you tell me a bit more about what's troubling you?"
        else:
            return "Thank you for sharing. Could you tell me more about how you're feeling?"