import unittest
from ticket import Ticket

class TestTicket(unittest.TestCase):

    def test_new_ticket_starts_open(self):
        t=Ticket(1, "Test title", "Test description")
        self.assertEqual(t.status, "open")

    def test_close_changes_status(self):
        t=Ticket(1, "Test title", "Test description")
        t.close()
        self.assertEqual(t.status, "closed")

    def test_to_dict_returns_correct_data(self):
        t=Ticket(1, "Test title", "Test description")
        result=t.to_dict()
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["title"], "Test title")
        self.assertEqual(result["status"], "open")

if __name__ == "__main__":
    unittest.main()