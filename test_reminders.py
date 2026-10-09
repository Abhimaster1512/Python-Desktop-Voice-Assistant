from database.reminder import (
    create_reminder,
    get_reminders,
    complete_reminder,
    delete_reminder
)


user_id = 1


# Create Reminder
print(
    create_reminder(
        user_id,
        "Submit MCA Project",
        "2026-06-20 17:00"
    )
)


# Read Reminders
print("\nYour Reminders:")

reminders = get_reminders(user_id)

for reminder in reminders:
    print(reminder)


# Complete Reminder
print(
    complete_reminder(1)
)


# Delete Reminder
print(
    delete_reminder(1)
)