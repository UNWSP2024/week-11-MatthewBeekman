import tkinter as tk
root = tk.Tk()
root.title("Favorite Saying")
root.geometry("400x200")
saying_label = tk.Label(root, text="Nothing is impossible with God.",
                        font=("Helvetica", 12), padx=20, pady=20, wraplength=360, justify="center")
saying_label.pack()
root.mainloop()

# Matthew Beekman
# Program 1
# 11/13/2024