import sqlite3
from sqlite3 import Connection

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

def setup_database(conn: Connection) -> None:
    """
    Set up the database by dropping and creating the Track table.

    Args:
        conn (Connection): The SQLite connection object.
    """
    with conn:
        conn.execute('DROP TABLE IF EXISTS Track')
        conn.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')

def main() -> None:
    """
    Main function to create and set up the SQLite database.
    """
    db_name = 'music.sqlite'
    try:
        conn = create_connection(db_name)
        setup_database(conn)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
