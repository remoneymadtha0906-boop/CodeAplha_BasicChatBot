def chatbot():

    print("===================================")
    print("       WELCOME TO CHATBOT")
    print("===================================")
    print("Hello! I am your Python Chatbot.")
    print("You can talk to me.")
    print("Type 'bye' to exit.")

    while True:

        user = input("\nYou: ").lower().strip()

        if user == "hello" or user == "hi" or user == "hey":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "what can you do":
            print("Bot: I can chat with you and answer simple questions.")

        elif user == "thank you" or user == "thanks":
            print("Bot: You're welcome!")

        elif user == "good morning":
            print("Bot: Good morning! Have a nice day.")

        elif user == "good night":
            print("Bot: Good night! Sweet dreams.")

        elif user == "bye" or user == "exit":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
