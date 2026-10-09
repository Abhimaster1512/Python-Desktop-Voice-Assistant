from core.note_handler import (
    create_voice_note,
    read_voice_notes
)
from nlp.intent_classifier import predict_intent
from chatbot.ai_chat import ask_ai
from automation.applicationcontrol import open_application
from automation.browser import open_website, google_search
from automation.calculator import calculate
from automation.datetime_info import get_time, get_date
from automation.weather import get_weather
from automation.news import get_news
from automation.volume_ss import (
    take_screenshot,
    shutdown_system,
    restart_system,
    lock_system
)


def process_command(command, listener=None, speaker=None):

    command = command.lower()

    intent, confidence = predict_intent(command)

    print(f"Predicted Intent: {intent}")
    print(f"Confidence: {confidence:.2f}")

    # Applications
    if confidence < 0.20:
        print("Unknown command. Sending to AI...")
        return ask_ai(command)
    if intent == "open_application":
        return open_application(command)


    # Websites
    elif intent == "open_website":
        return open_website(command)


    # Google Search
    elif intent == "google_search":
        return google_search(command)


    # Time
    elif intent == "time":
        return get_time()


    # Date
    elif intent == "date":
        return get_date()


    # Calculator
    elif intent == "calculator":
        expression = command.replace("calculate", "")
        return calculate(expression)


    # Weather
    elif intent == "weather":

        if listener:
            print("Please tell me the city name")
            city = listener.listen()
            return get_weather(city)

        return "Please provide city name"


    # News
    elif intent == "news":
        return get_news()


    # Screenshot
    elif intent == "screenshot":
        return take_screenshot()


    # Shutdown
    elif intent == "shutdown":
        return shutdown_system()


    # Restart
    elif intent == "restart":
        return restart_system()


    # Lock System
    elif intent == "lock":
        return lock_system()
    
    elif intent == "note_create":
        return create_voice_note(listener, speaker)


    elif intent == "note_read":
        return read_voice_notes()


    else:
        return "Sorry, I don't understand this command."