import sqlite3
import pytest

def get_user(user_id):
    if not isinstance(user_id, int):
        raise TypeError("User ID must be an integer.")
    if user_id < 0:
        raise ValueError("User ID must be a non-negative integer.")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result
```

Note: I have added pytest to the install_requires and tests_require list in the setup.py file. This will ensure that pytest is installed when the package is installed. I have also added a pytest import statement in the db/query.py file to avoid a future error when running the tests.