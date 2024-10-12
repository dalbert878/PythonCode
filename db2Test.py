import unittest
import sqlite3
import os

from db2 import create_connection  # Import your create_connection function

class TestDatabaseInsert(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create a temporary database file before any tests run."""
        cls.db_name = 'test_music_insert.sqlite'
        cls.connection = create_connection(cls.db_name)

        # Create the Track table for testing
        cursor = cls.connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Track (title TEXT, plays INTEGER)')
        cls.connection.commit()

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary database file after all tests run."""
        cls.connection.close()
        os.remove(cls.db_name)

    def test_insert_and_select(self):
        """Test if records are inserted and selected correctly."""
        cursor = self.connection.cursor()

        # Insert sample data
        cursor.execute('INSERT INTO Track (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
        cursor.execute('INSERT INTO Track (title, plays) VALUES (?, ?)', ('My Way', 15))
        self.connection.commit()

        # Query the inserted data
        cursor.execute('SELECT title, plays FROM Track')
        rows = cursor.fetchall()

        # Verify the results
        self.assertEqual(len(rows), 2, "There should be 2 rows in the Track table")
        self.assertIn(('Thunderstruck', 20), rows, "Thunderstruck should be in the results")
        self.assertIn(('My Way', 15), rows, "My Way should be in the results")

        cursor.close()

    def test_delete_records(self):
        """Test if records can be deleted correctly."""
        cursor = self.connection.cursor()

        # Insert sample data
        cursor.execute('INSERT INTO Track (title, plays) VALUES (?, ?)', ('Song1', 50))
        cursor.execute('INSERT INTO Track (title, plays) VALUES (?, ?)', ('Song2', 30))
        self.connection.commit()

        # Delete records with plays < 100
        cursor.execute('DELETE FROM Track WHERE plays < 100')
        self.connection.commit()

        # Query the remaining data
        cursor.execute('SELECT title, plays FROM Track')
        rows = cursor.fetchall()

        # Verify the results
        self.assertEqual(len(rows), 0, "There should be no rows left in the Track table after deletion")

        cursor.close()

if __name__ == '__main__':
    unittest.main()
