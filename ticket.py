from datetime import datetime

class Ticket:
    def __init__(self, ticket_id, title, description, status="open", created_at=None, closed_at=None):
        self.id = ticket_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.now().strftime("%m/%d/%Y %H:%M")
        self.closed_at = closed_at

    def close(self):
        self.status = "closed"
        self.closed_at = datetime.now().strftime("%m/%d/%Y %H:%M")

    def display(self):
        print(f"ID: {self.id}| Title: {self.title}| Description: {self.description}| Status: {self.status}| Created: {self.created_at}| Closed: {self.closed_at}")

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "status": self.status, "created_at": self.created_at, "closed_at": self.closed_at}
    