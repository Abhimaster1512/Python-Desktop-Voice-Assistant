import bcrypt
from database.connection import get_connection


def register_user(username, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    # Convert password to encrypted hash
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    try:
        cursor.execute(
            """
            INSERT INTO users(username, email, password)
            VALUES (?, ?, ?)
            """,
            (username, email, hashed_password)
        )

        conn.commit()

        return "User registered successfully"

    except Exception as e:
        return f"Registration failed: {e}"

    finally:
        conn.close()


def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT user_id, username, password
        FROM users
        WHERE email = ?
        """,
        (email,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        user_id = user[0]
        username = user[1]
        stored_password = user[2]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_password
        ):

            return {
                "user_id": user_id,
                "username": username
            }

    return None