import unittest
import sqlite3
import os


from db1 import create_connection

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create a temporary database file before any tests run."""
        cls.db_name = 'test_music.sqlite'
        cls.connection = create_connection(cls.db_name)

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary database file after all tests run."""
        cls.connection.close()
        os.remove(cls.db_name)

    def test_create_table(self):
        """Test if the Track table is created successfully."""
        cursor = self.connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS Track')  # Ensure the table is dropped for testing
        cursor.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')

        # Check if the table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Track';")
        result = cursor.fetchone()
        self.assertIsNotNone(result, "Track table should be created")
        self.assertEqual(result[0], 'Track', "Table name should be 'Track'")

        cursor.close()

if __name__ == '__main__':
    unittest.main()
