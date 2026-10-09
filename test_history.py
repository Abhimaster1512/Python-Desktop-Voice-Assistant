from database.history import (
    save_history,
    get_history,
    clear_history
)


user_id = 1


# Save command
print(
    save_history(
        user_id,
        "Open Chrome",
        "Opening Chrome"
    )
)


print("\nCommand History:")

history = get_history(user_id)

for item in history:
    print(item)


# Uncomment this if you want to delete history
# print(clear_history(user_id))