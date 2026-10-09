from database.connection import get_connection


# Create Note
def create_note(user_id, title, content):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO notes(user_id, title, content)
        VALUES (?, ?, ?)
        """,
        (user_id, title, content)
    )

    conn.commit()
    conn.close()

    return "Note created successfully"


# Read All Notes
def get_notes(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT note_id, title, content, created_at
        FROM notes
        WHERE user_id = ?
        """,
        (user_id,)
    )

    notes = cursor.fetchall()

    conn.close()

    return notes


# Update Note
def update_note(note_id, new_content):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE notes
        SET content = ?
        WHERE note_id = ?
        """,
        (new_content, note_id)
    )

    conn.commit()
    conn.close()

    return "Note updated successfully"


# Delete Note
def delete_note(note_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM notes
        WHERE note_id = ?
        """,
        (note_id,)
    )

    conn.commit()
    conn.close()

    return "Note deleted successfully"