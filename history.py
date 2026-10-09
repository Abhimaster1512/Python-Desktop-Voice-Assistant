from .connection import get_connection


# Save command history
def save_history(user_id, command, response):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(user_id, command, response)
        VALUES (?, ?, ?)
        """,
        (user_id, command, response)
    )

    conn.commit()
    conn.close()

    return "History saved successfully"


# Get all history of a user
def get_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT command, response, created_at
        FROM history
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    records = cursor.fetchall()

    conn.close()

    return records


# Delete all history of a user
def clear_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM history
        WHERE user_id = ?
        """,
        (user_id,)
    )

    conn.commit()
    conn.close()

    return "Command history cleared successfully"