import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?", "I'm fine! What about you?"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care."],
    "default": ["I'm not sure how to respond to that.", "Could you rephrase that?", "Sorry, I don't understand."]
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Match user input with predefined responses
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(responses["default"])

# Main execution
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break
        else:
            print("Chatbot:", chatbot_response(user_input))
