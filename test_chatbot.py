from chatbot.ai_chat import ask_ai


while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ask_ai(question)

    print("Assistant:", answer)