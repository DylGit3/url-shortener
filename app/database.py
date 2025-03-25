import sqlite3


def init_db():
    db = sqlite3.connect("urls.db", check_same_thread=False)
    db.execute(
        "CREATE TABLE IF NOT EXISTS urls (short TEXT PRIMARY KEY, long TEXT, clicks INTEGER DEFAULT 0)")
    return db


def save_url(db, short_code, long_url):
    db.execute("INSERT INTO urls (short, long) VALUES (?, ?)",
               (short_code, long_url))
    db.commit()


def get_url(db, short_code):
    return db.execute("SELECT long, clicks FROM urls WHERE short = ?", (short_code,)).fetchone()
