#!/usr/bin/python3
import MySQLdb
import unittest

class TestStateFunctions(unittest.TestCase):
    def setUp(self):
        # Connect to the test database
        self.db = MySQLdb.connect(host="localhost", user="testuser", passwd="testpass", db="testdb")
        self.cursor = self.db.cursor()

    def test_add_state(self):
        # Get the number of states before adding a new one
        self.cursor.execute("SELECT COUNT(*) FROM states")
        before_count = self.cursor.fetchone()[0]

        # Add a new state to the database
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")

        # Get the number of states after adding the new one
        self.cursor.execute("SELECT COUNT(*) FROM states")
        after_count = self.cursor.fetchone()[0]

        # Check that the number of states increased by one
        self.assertEqual(before_count + 1, after_count)

    def tearDown(self):
        # Clean up after the test
        self.db.rollback()
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    unittest.main()
