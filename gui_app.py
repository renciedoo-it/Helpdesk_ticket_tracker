import tkinter as tk
from tkinter import messagebox
from ticket import Ticket
from storage import load_tickets, save_tickets

tickets = load_tickets()

window = tk.Tk()
window.title("Helpdesk Ticket tracker")
window.geometry("500x400")

tk.Label(window, text="Title: ").pack()
title_entry = tk.Entry(window, width=50)
title_entry.pack()

tk.Label(window, text="Description: ").pack()
description_entry = tk.Entry(window, width=50)
description_entry.pack()

ticket_listbox = tk.Listbox(window, width=70, height=15)
ticket_listbox.pack()

def refresh_list():
    ticket_listbox.delete(0, tk.END)
    for ticket in tickets:
        ticket_listbox.insert(tk.END, f"ID: {ticket.id} | {ticket.title} | Status: {ticket.status}")

def add_ticket():
    title = title_entry.get()
    description = description_entry.get()

    if title.strip() == "" or description.strip() == "":
        messagebox.showwarning("Missing info", "Title and description cannot be empty.")
        return

    ticket_id = len(tickets) + 1
    new_ticket = Ticket(ticket_id, title, description)
    tickets.append(new_ticket)
    save_tickets(tickets)

    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

    refresh_list()

add_button = tk.Button(window, text="Add Ticket", command=add_ticket)
add_button.pack()

refresh_list()
window.mainloop()