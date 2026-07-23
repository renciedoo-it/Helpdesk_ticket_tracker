import json
import os
from ticket import Ticket

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tickets.json")

def load_tickets():
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    load_tickets = []
    return [Ticket(t["id"], t["title"], t["description"],t["status"], t.get("created_at"), t.get("closed_at")) for t in data]

def save_tickets(tickets):
    dict_list = [ticket.to_dict() for ticket in tickets]

    with open(FILE_PATH, "w") as file:
        json.dump(dict_list, file, indent=4)