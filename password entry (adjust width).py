import tkinter as tk

root = tk.Tk()
root.title("Python Entry Widget")
root.geometry("400x100")

instruction_label = tk.Label(root, text="Enter your password:")
instruction_label.pack(pady=10)

entry = tk.Entry(root, width=50, show="*")
entry.pack(pady=5)
#show="":shows a certain character, likely ginagamit sya para itago iinput ng user for privacy purposes 
#width= : para maadjust yung width ng entry widget

root.mainloop()
