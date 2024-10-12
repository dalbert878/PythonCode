import sqlite3
from sqlite3 import Connection, Cursor

def create_connection(db_name: str) -> Connection:
    """
    Create a database connection to the specified SQLite database.

    Args:
        db_name (str): The name of the database file.

    Returns:
        Connection: SQLite connection object.
    """
    try:
        return sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def insert_tracks(cursor: Cursor) -> None:
    """
    Insert sample track data into the Track table.

    Args:
        cursor (Cursor): SQLite cursor object.
    """
    tracks = [
        ('Thunderstruck', 20),
        ('My Way', 15)
    ]
    cursor.executemany('INSERT INTO Track (title, plays) VALUES (?, ?)', tracks)

def display_tracks(cursor: Cursor) -> None:
    """
    Display all tracks from the Track table.

    Args:
        cursor (Cursor): SQLite cursor object.
    """
    cursor.execute('SELECT title, plays FROM Track')
    print('Tracks:')
    for title, plays in cursor.fetchall():
        print(f"Title: {title}, Plays: {plays}")

def delete_tracks(cursor: Cursor) -> None:
    """
    Delete tracks from the Track table where plays are less than 100.

    Args:
        cursor (Cursor): SQLite cursor object.
    """
    cursor.execute('DELETE FROM Track WHERE plays < 100')

def main() -> None:
    """
    Main function to handle the database operations.
    """
    db_name = 'music.sqlite'
    try:
        conn = create_connection(db_name)
        with conn:
            cursor = conn.cursor()
            insert_tracks(cursor)
            display_tracks(cursor)
            delete_tracks(cursor)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
