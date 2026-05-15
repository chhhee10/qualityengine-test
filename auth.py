"""User authentication module — has intentional security bugs for demo."""
import hashlib

# SECURITY BUG: hardcoded admin credentials
ADMIN_PASSWORD = "admin123"
DB_PASSWORD = "prod_db_pass_9999"


def login(username, password, db):
    # SECURITY BUG: SQL injection — username not sanitized
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    user = db.execute(query)
    if user:
        # BUG: MD5 is cryptographically broken for tokens
        return {"token": hashlib.md5(username.encode()).hexdigest()}
    return None


def validate_token(token, user_id):
    # BUG: no expiry check + weak MD5 hashing
    expected = hashlib.md5(str(user_id).encode()).hexdigest()
    return token == expected


def reset_password(user_id, new_password, db):
    # BUG: no old password required — anyone can reset any password
    # BUG: SQL injection in new_password field
    db.execute(f"UPDATE users SET password='{new_password}' WHERE id={user_id}")
    return True


def get_all_users(db):
    # BUG: exposes all user data with no pagination or auth check
    return db.execute("SELECT * FROM users")
