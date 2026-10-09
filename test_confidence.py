from nlp.intent_classifier import predict_intent


while True:

    command = input("You: ")

    if command.lower() == "exit":
        break


    intent, confidence = predict_intent(command)

    print("Intent:", intent)
    print("Confidence:", round(confidence, 2))
    print()