"""DELIBERATELY INSECURE — demo only."""
import os
import sqlite3

API_SECRET = "sk-live-hardcoded-demo-key-12345"
DB_PATH = "/tmp/demo.db"


def run_user_code(expression: str) -> object:
    return eval(expression)


def run_shell(cmd: str) -> int:
    return os.system(cmd)


def login(username: str, password: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = f"SELECT 1 FROM users WHERE name='{username}' AND pass='{password}'"
    cur.execute(query)
    return cur.fetchone() is not None
