import sqlite3 as sq
import hashlib

## OUT OF COMMISSION LOL
# Create a database that gives each user their own vault
def udb_connect(username):
    with sq.connect(username+".db") as udb:
        u_cursor = udb.cursor()

    u_cursor.execute("""
    CREATE TABLE IF NOT EXISTS vault(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    website TEXT NOT NULL);
    """)



