import ollama


def ask_ai(question):

    try:

        response = ollama.chat(
            model="llama3.1:8b",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an AI voice assistant.
                    Give short, clear, and accurate answers.
                    Your responses will be spoken using text to speech.
                    """
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response["message"]["content"]

        return answer

    except Exception as e:
        return f"AI Error: {e}"