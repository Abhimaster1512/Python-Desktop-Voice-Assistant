import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")

            # Reduce background noise
            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            
            text = self.recognizer.recognize_google(audio)

            print(f"You: {text}")

            return text.lower()

        except sr.UnknownValueError:
            return "Sorry, I did not understand."

        except sr.RequestError:
            return "Speech service is unavailable."