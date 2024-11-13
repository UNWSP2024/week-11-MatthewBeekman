import tkinter as tk
from tkinter import messagebox
def show_info():
    name = "Matthew Beekman"
    address = "2606 96th St E, Inver Grove Heights, MN"
    messagebox.showinfo("Information", f"Name: {name}\nAddress: {address}")
def quit_app():
    root.quit()
root = tk.Tk()
root.title("Info Display")
show_info_button = tk.Button(root, text="Show Info", command=show_info)
show_info_button.pack(pady=10)
quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(pady=10)
root.mainloop()

# Matthew Beekman
# Program 2
# 11/13/2024