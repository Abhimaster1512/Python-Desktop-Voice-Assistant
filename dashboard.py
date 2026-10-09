import customtkinter as ctk

from authentication.session import get_user, logout

from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech

from core.command_router import process_command

from database.history import save_history


class Dashboard:

    def __init__(self):

        # Window setup
        self.root = ctk.CTk()

        self.root.title("AI Voice Assistant")
        self.root.geometry("700x550")

        # Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Logged-in user
        self.user = get_user()

        # Voice objects
        self.listener = SpeechToText()
        self.speaker = TextToSpeech()

        # Title
        title = ctk.CTkLabel(
            self.root,
            text="🤖 AI Voice Assistant",
            font=("Arial", 25, "bold")
        )
        title.pack(pady=10)

        # User name
        self.user_label = ctk.CTkLabel(
            self.root,
            text=f"User: {self.user['username']}",
            font=("Arial", 16)
        )
        self.user_label.pack()

        # Status
        self.status_label = ctk.CTkLabel(
            self.root,
            text="Status: Ready",
            font=("Arial", 14)
        )
        self.status_label.pack(pady=10)

        # Conversation box
        self.chat_box = ctk.CTkTextbox(
            self.root,
            width=600,
            height=280,
            font=("Arial", 14)
        )
        self.chat_box.pack(pady=20)

        self.chat_box.insert(
            "end",
            "Assistant: Hello, how can I help you today?\n\n"
        )

        # Button frame
        button_frame = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )
        button_frame.pack(pady=20)

        # Listen button
        listen_button = ctk.CTkButton(
            button_frame,
            text="🎤 Start Listening",
            width=180,
            command=self.start_listening
        )
        listen_button.grid(
            row=0,
            column=0,
            padx=10
        )

        # Clear chat button
        clear_button = ctk.CTkButton(
            button_frame,
            text="🧹 Clear Chat",
            width=120,
            command=self.clear_chat
        )
        clear_button.grid(
            row=0,
            column=1,
            padx=10
        )

        # Logout button
        logout_button = ctk.CTkButton(
            button_frame,
            text="🚪 Logout",
            width=100,
            command=self.logout
        )
        logout_button.grid(
            row=0,
            column=2,
            padx=10
        )


    def start_listening(self):

        # Update status
        self.status_label.configure(
            text="Status: Listening..."
        )
        self.root.update()

        # Get voice command
        command = self.listener.listen()

        if not command:
            self.status_label.configure(
                text="Status: Ready"
            )
            return

        # Show user command
        self.chat_box.insert(
            "end",
            f"You: {command}\n"
        )
        self.chat_box.see("end")

        # Processing
        self.status_label.configure(
            text="Status: Processing..."
        )
        self.root.update()

        # Process command
        response = process_command(
            command,
            self.listener,
            self.speaker
        )

        # Show assistant response
        self.chat_box.insert(
            "end",
            f"Assistant: {response}\n\n"
        )
        self.chat_box.see("end")

        # Speak response
        self.speaker.speak(response)

        # Save history
        save_history(
            self.user["user_id"],
            command,
            response
        )

        # Back to ready state
        self.status_label.configure(
            text="Status: Ready"
        )


    def clear_chat(self):

        self.chat_box.delete(
            "1.0",
            "end"
        )

        self.chat_box.insert(
            "end",
            "Assistant: Hello, how can I help you today?\n\n"
        )


    def logout(self):

        logout()

        self.root.destroy()


    def run(self):

        self.root.mainloop()