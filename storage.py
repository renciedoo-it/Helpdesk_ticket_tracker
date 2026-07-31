import sqlite3
import sys
import os
from ticket import Ticket

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "tickets.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            status TEXT,
            created_at TEXT,
            closed_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def load_tickets():
    create_table()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, status, created_at, closed_at FROM tickets")
    rows = cursor.fetchall()
    conn.close()

    return [Ticket(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

def save_tickets(tickets):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets")

    for ticket in tickets:
        cursor.execute(
            "INSERT INTO tickets (id, title, description, status, created_at, closed_at) VALUES (?, ?, ?, ?, ?, ?)",
            (ticket.id, ticket.title, ticket.description, ticket.status, ticket.created_at, ticket.closed_at)
        )

    conn.commit()
    conn.close()
