from app.db import wait_for_db

def test_db_connection():

    connection = wait_for_db()
    assert connection is not None

    cursor = connection.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    assert result is not None
    assert result[0] == 1

    cursor.close()
    connection.close()