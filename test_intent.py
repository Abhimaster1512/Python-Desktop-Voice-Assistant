from nlp.intent_classifier import predict_intent


while True:

    command = input("You: ")

    if command.lower() == "exit":
        break

    intent = predict_intent(command)

    print("Predicted Intent:", intent)