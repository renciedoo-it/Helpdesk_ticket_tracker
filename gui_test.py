import tkinter as tk

def on_button_click():
    print("Button was clicked!")

window = tk.Tk()
window.geometry("400x200")

label = tk.Label(window, text="Welcome!")
label.pack()

button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

window.mainloop()