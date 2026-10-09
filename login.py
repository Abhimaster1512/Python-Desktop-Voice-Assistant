from database.user import login_user
from authentication.session import set_user


def login():

    print("\n===== AI Assistant Login =====")

    email = input("Enter Email: ")
    password = input("Enter Password: ")


    user = login_user(email, password)


    if user:

        set_user(user)

        print(
            f"Welcome {user['username']}"
        )

        return True


    print("Invalid email or password")

    return False