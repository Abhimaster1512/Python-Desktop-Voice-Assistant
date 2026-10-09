from database.notes import (
    create_note,
    get_notes,
    update_note,
    delete_note
)


user_id = 1


# Create Note
print(
    create_note(
        user_id,
        "Shopping List",
        "Buy milk and eggs"
    )
)


# Read Notes
print("\nAll Notes:")
notes = get_notes(user_id)

for note in notes:
    print(note)


# Update Note
print(
    update_note(
        1,
        "Buy milk, eggs and bread"
    )
)


# Delete Note
print(
    delete_note(1)
)