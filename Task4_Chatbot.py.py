def run_basic_chatbot():
    print("--- CodeAlpha Basic Chatbot ---")
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' or 'exit' to end the chat.")

    # Main chat loop
    while True:
        # Get input from the user and convert to lowercase to make matching easier
        user_input = input("\nYou: ").lower().strip()

        # Predefined rule-based replies using if-elif
        if user_input in ["hi", "hello", "hey", "greetings"]:
            print("Chatbot: Hi! It's nice to meet you.")
            
        elif user_input in ["how are you", "how are you?", "how are you doing"]:
            print("Chatbot: I'm fine, thanks!")
            
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I am a basic rule-based chatbot created for a Python project.")
            
        elif user_input in ["what can you do", "help"]:
            print("Chatbot: I can respond to simple greetings and questions. Try saying 'hello' or asking how I am!")
            
        # Exit condition
        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break  # This breaks the loop and ends the function
            
        # Fallback response for unknown inputs
        else:
            print("Chatbot: I'm sorry, I don't understand that. I only have a few predefined responses right now.")

# Execute the function
if __name__ == "__main__":
    run_basic_chatbot()