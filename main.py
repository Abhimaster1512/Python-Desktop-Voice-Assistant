from voice.text_to_speech import TextToSpeech
from voice.speech_to_text import SpeechToText

from core.command_router import process_command

from authentication.login import login
from authentication.session import get_user

from database.history import save_history


def main():

    # Login before starting assistant
    success = login()

    if not success:
        print("Access denied")
        return


    user = get_user()


    speaker = TextToSpeech()
    listener = SpeechToText()


    speaker.speak(
        f"Hello {user['username']}, I am your AI voice assistant. How can I help you?"
    )


    while True:

        command = listener.listen()


        # Skip empty command
        if not command:
            continue


        # Exit command
        if "exit" in command or "stop" in command:
            
            response = "Goodbye. Have a nice day."

            speaker.speak(response)

            save_history(
                user["user_id"],
                command,
                response
            )

            break


        # Process command using NLP
        response = process_command(
            command,
            listener,
            speaker
        )


        # Speak response
        speaker.speak(response)


        # Save interaction in database
        save_history(
            user["user_id"],
            command,
            response
        )


if __name__ == "__main__":
    main()