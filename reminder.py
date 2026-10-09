from database.connection import get_connection


# Create Reminder
def create_reminder(user_id, task, reminder_time):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reminders(user_id, task, reminder_time)
        VALUES (?, ?, ?)
        """,
        (user_id, task, reminder_time)
    )

    conn.commit()
    conn.close()

    return "Reminder created successfully"


# Read All Reminders
def get_reminders(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT reminder_id, task, reminder_time, status
        FROM reminders
        WHERE user_id = ?
        """,
        (user_id,)
    )

    reminders = cursor.fetchall()

    conn.close()

    return reminders


# Update Reminder Status
def complete_reminder(reminder_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE reminders
        SET status = 'completed'
        WHERE reminder_id = ?
        """,
        (reminder_id,)
    )

    conn.commit()
    conn.close()

    return "Reminder marked as completed"


# Delete Reminder
def delete_reminder(reminder_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM reminders
        WHERE reminder_id = ?
        """,
        (reminder_id,)
    )

    conn.commit()
    conn.close()

    return "Reminder deleted successfully"