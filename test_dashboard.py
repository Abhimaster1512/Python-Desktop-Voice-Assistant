from authentication.session import set_user
from gui.dashboard import Dashboard
from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech

from core.command_router import process_command

from database.history import save_history

set_user(
    {
        "user_id": 1,
        "username": "Abhijeet"
    }
)


app = Dashboard()

app.run()
