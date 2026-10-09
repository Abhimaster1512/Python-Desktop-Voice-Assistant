from database.notes import create_note, get_notes
from authentication.session import get_user


def create_voice_note(listener, speaker):

    user = get_user()

    speaker.speak("What should be the title of your note?")

    title = listener.listen()

    speaker.speak("What should I write in the note?")

    content = listener.listen()

    result = create_note(
        user["user_id"],
        title,
        content
    )

    return result


def read_voice_notes():

    user = get_user()

    notes = get_notes(user["user_id"])

    if not notes:
        return "You don't have any notes."

    response = "Your notes are: "

    for note in notes:
        response += (
            f"{note[1]}. "
            f"{note[2]}. "
        )

    return response