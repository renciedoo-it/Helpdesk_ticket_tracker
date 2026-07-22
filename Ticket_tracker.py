
import json
import os

class Ticket:
    def __init__(self, ticket_id, title, description, status="open"):
        self.id = ticket_id
        self.title = title
        self.description = description
        self.status = status

    def close(self):
        self.status = "closed"

    def display(self):
        print(f"ID: {self.id} | Title: {self.title} | Description: {self.description} | Status: {self.status}")

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "status": self.status}
       

FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tickets.json")

def load_tickets():
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    loaded_tickets = []
    for t in data:
        loaded_tickets.append(Ticket(t["id"], t["title"], t["description"], t["status"]))
    return loaded_tickets

def save_tickets(tickets):
    dict_list = []
    for ticket in tickets:
        dict_list.append(ticket.to_dict())

    with open(FILE_PATH, "w") as file:
        json.dump(dict_list, file, indent=4)

tickets = load_tickets()

while True:
    print("\n==== Helpdesk Ticketing System ====")
    print("1. Add Ticket")
    print("2. View Tickets")
    print("3. Search Tickets")
    print("4. Close Ticket")
    print("5. Exit")

    choice = input("Choose your option: ")

    if choice == "1":
        title = input("Enter ticket title: ")

        if title.strip() == "":
            print("Ticket title cannot be empty. Please try again.")
            continue
        
        ticket_id = len(tickets) + 1
        description = input("Enter ticket description: ")

        if description.strip() == "":
            print("Ticket description cannot be empty. Please try again.")
            continue

        new_ticket = Ticket(ticket_id, title, description)
        tickets.append(new_ticket)
        save_tickets(tickets)

    elif choice == "2":
        print("\nTicket List: ")

        for ticket in tickets:
            ticket.display()
    
    elif choice == "3":
        
        search_input = input("Enter Ticket ID: ")

        try:
            search_id = int(search_input)
        except ValueError:
            print("Invalid input. Please enter a valid Ticket ID.")
            continue
        

        found = False

        for ticket in tickets:
            if ticket.id == search_id:
                ticket.display()
                found = True

            if not found:
                print("Ticket not found.")
    
    elif choice == "4":
        close_input = input("Enter Ticket ID to close: ")

        try:
            close_id = int(close_input)
        except ValueError:
            print("Invalid input. Please enter a valid Ticket ID.")
            continue

        found = False

        for ticket in tickets:
            if ticket.id == close_id:
                ticket.close()
                print(f"Ticket ID {close_id} has been closed.")
                found = True
                save_tickets(tickets)

        if not found:
            print("Ticket not found.")

    elif choice == "5":
        print("Exiting the Helpdesk Ticketing System.")
        break

    else:
        print("Invalid option. Please try again.")