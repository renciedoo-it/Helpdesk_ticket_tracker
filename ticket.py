class Ticket:
    def __init__(self, ticket_id, title, description, status="open"):
        self.id = ticket_id
        self.title = title
        self.description = description
        self.status = status

    def close(self):
        self.status = "closed"

    def display(self):
        print(f"ID: {self.id}| Title: {self.title}| Description: {self.description}| Status: {self.status}")

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "status": self.status}
    