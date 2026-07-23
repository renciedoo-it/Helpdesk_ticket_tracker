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
    for t in data:
        load_tickets.append(Ticket(t["id"], t["title"], t["description"], t["status"], t.get("created_at"), t.get("closed_at")))
    return load_tickets

def save_tickets(tickets):
    dict_list = []
    for ticket in tickets:
        dict_list.append(ticket.to_dict())

    with open(FILE_PATH, "w") as file:
        json.dump(dict_list, file, indent=4)