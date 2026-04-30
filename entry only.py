import tkinter as tk

root = tk.Tk()
root.title("Entry Box")
root.geometry("200x200")

entry = tk.Entry(root)
entry.pack(pady=50, padx=50)

root.mainloop()