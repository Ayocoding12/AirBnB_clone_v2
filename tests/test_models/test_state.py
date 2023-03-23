#!/usr/bin/python3
import MySQLdb
import pytest

@pytest.fixture
def db():
    # Connect to the test database
    conn = MySQLdb.connect(host="localhost", user="testuser", passwd="testpass", db="testdb")
    cursor = conn.cursor()

    yield cursor

    # Clean up after the test
    conn.rollback()
    cursor.close()
    conn.close()

def test_add_state(db):
    # Get the number of states before adding a new one
    db.execute("SELECT COUNT(*) FROM states")
    before_count = db.fetchone()[0]

    # Add a new state to the database
    db.execute("INSERT INTO states (name) VALUES ('California')")

    # Get the number of states after adding the new one
    db.execute("SELECT COUNT(*) FROM states")
    after_count = db.fetchone()[0]

    # Check that the number of states increased by one
    assert before_count + 1 == after_count
