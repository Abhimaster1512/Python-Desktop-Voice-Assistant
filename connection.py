import sqlite3


def get_connection():
    connection = sqlite3.connect("assistant.db")
    return connection