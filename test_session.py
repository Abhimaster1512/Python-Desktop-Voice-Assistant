from authentication.session import (
    set_user,
    get_user,
    logout
)


user = {
    "user_id": 1,
    "username": "Abhijeet"
}


set_user(user)

print(get_user())


logout()

print(get_user())