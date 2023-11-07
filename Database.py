import sqlite3 as sq
import hashlib

def db_connect():
    with sq.connect('vault.db') as db:
        cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vault(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    website TEXT NOT NULL);
    """)

def udb_connect():
    with sq.connect('users.db') as udb:
        u_cursor = udb.cursor()

    u_cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL);
    """)

# Create a database that corresponds with each user in the
# user database

