from chat import chat

conversation = []

while True:
    user_input = input("You: ")
    reply = chat(conversation, user_input)
    print(f"Claude: {reply}\n")