import tkinter as tk

def userInput(event=None):
    text = entry.get()
    result_label.config(text=f"You entered: {text}")
#yung .get() method like yung literal na meaning nya which is kukunin yung in-input ng user tas isasave
#sa variable na 'text'.
#sa line 5, since yung sa line 25 and 26 may initialize na empty label widget, ginamit yung .config() para
#ma-update yung 'text' variable.

root = tk.Tk()
root.title("Python Entry Project")
root.geometry("300x200")
#line 11: for creating the main window ng gui
#line 12: title ng main window
#line13: size ng window na mag ppop up

instruction_label = tk.Label(root, text="Enter your name:")
instruction_label.pack(pady=10)
#line 18 and 19: widget/title na nasa loob ng main window (for instructions)
#!!hindi sya title ng main window, pero title na nasa loob ng main win
#(pady=10 is like y-axis sa cartesian plane (vertical space))

entry = tk.Entry(root)
entry.pack(pady=5)
#line 23 & 24: entry widget, loob pa rin ng main window

entry.bind('<Return>', userInput)
#.bind() method for binding a key or mouse click sa isang function. for example dyan ang nilagay ko is '<return>'
# where if ang user is nagclick ng enter button gagawin ng program yung isang function which is yung
# userInput

submit_button = tk.Button(root, text="Submit", command=userInput)
submit_button.pack(pady=10)
#line for a button na clickable pag pinindot ng user yan, may nilagay na command which is yung user input
# na gagawin ng program after maclick yung button.
#!!same lang sya sa .bind() kaso eto for manual na pag pindot ng isang button

result_label = tk.Label(root, text="")
result_label.pack(pady=10)
#eto yung initial na itsura ng result label, empty pa (text=""), pero magbabago yan every time na may sinubmit ang user
#na name.


root.mainloop()