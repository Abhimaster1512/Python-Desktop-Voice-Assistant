from database.user import register_user, login_user


# Register
print(
    register_user(
        "Abhijeet",
        "abhijeet@gmail.com",
        "123456"
    )
)


# Login
user = login_user(
    "abhijeet@gmail.com",
    "123456"
)

if user:
    print("Login successful")
    print(user)

else:
    print("Invalid email or password")