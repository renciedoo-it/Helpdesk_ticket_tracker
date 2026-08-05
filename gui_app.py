import tkinter as tk
from tkinter import messagebox
from ticket import Ticket
from storage import load_tickets, save_tickets

tickets = load_tickets()
selected_ticket = None

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

def clear_form():
    global selected_ticket
    title_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    selected_ticket = None

def on_select(event):
    global selected_ticket
    selection = ticket_listbox.curselection()
    if not selection:
        return
    index = selection[0]
    selected_ticket = tickets[index]
    title_entry.delete(0, tk.END)
    title_entry.insert(0, selected_ticket.title)
    description_entry.delete(0, tk.END)
    description_entry.insert(0, selected_ticket.description)

ticket_listbox.bind("<<ListboxSelect>>", on_select)

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

    clear_form()
    refresh_list()

def update_ticket():
    if selected_ticket is None:
        messagebox.showwarning("No selection", "Please select a ticket to update.")
        return

    title = title_entry.get()
    description = description_entry.get()

    if title.strip() == "" or description.strip() == "":
        messagebox.showwarning("Missing info", "Title and description cannot be empty.")
        return

    selected_ticket.title = title
    selected_ticket.description = description
    save_tickets(tickets)

    clear_form()
    refresh_list()

def close_ticket():
    if selected_ticket is None:
        messagebox.showwarning("No selection", "Please select a ticket to close.")
        return

    selected_ticket.close()
    save_tickets(tickets)

    clear_form()
    refresh_list()

button_fram = tk.Frame(window)
button_fram.pack(pady=10)

add_button = tk.Button(button_fram, text="Add Ticket", command=add_ticket)
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_fram, text="Update Ticket", command=update_ticket)
update_button.grid(row=0, column=1, padx=5)

close_button = tk.Button(button_fram, text="Close Ticket", command=close_ticket)
close_button.grid(row=0, column=2, padx=5)


refresh_list()
window.mainloop()