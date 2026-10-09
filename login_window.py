import customtkinter as ctk
from gui.dashboard import Dashboard
from tkinter import messagebox

from database.user import login_user
from authentication.session import set_user


class LoginWindow:

    def __init__(self):

        # Window setup
        self.root = ctk.CTk()

        self.root.title("AI Voice Assistant Login")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        # Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        # Heading
        title = ctk.CTkLabel(
            self.root,
            text="🤖 AI Voice Assistant",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)


        # Email Label
        email_label = ctk.CTkLabel(
            self.root,
            text="Email"
        )
        email_label.pack(pady=5)


        # Email Entry
        self.email_entry = ctk.CTkEntry(
            self.root,
            width=250,
            height=40,
            placeholder_text="Enter your email"
        )
        self.email_entry.pack(pady=10)


        # Password Label
        password_label = ctk.CTkLabel(
            self.root,
            text="Password"
        )
        password_label.pack(pady=5)


        # Password Entry
        self.password_entry = ctk.CTkEntry(
            self.root,
            width=250,
            height=40,
            show="*",
            placeholder_text="Enter password"
        )
        self.password_entry.pack(pady=10)


        # Login Button
        login_button = ctk.CTkButton(
            self.root,
            text="Login",
            width=200,
            height=40,
            command=self.login
        )
        login_button.pack(pady=30)


    def login(self):

        email = self.email_entry.get()
        password = self.password_entry.get()


        if not email or not password:
            messagebox.showerror(
                "Error",
                "Please enter email and password"
            )
            return


        user = login_user(email, password)


        if user:

            set_user(user)

            messagebox.showinfo(
                "Success",
                f"Welcome {user['username']}"
            )

            self.root.destroy()
            dashboard = Dashboard()
            dashboard.run()


        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid email or password"
            )


    def run(self):

        self.root.mainloop()


if __name__ == "__main__":

    app = LoginWindow()

    app.run()