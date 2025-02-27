# Import Module
import tkinter as tk
from tkinter import scrolledtext

# compare function
def compare():
    input1 = box1.get("1.0", tk.END)
    input2 = box2.get("1.0", tk.END)
    if input1 == input2:
        label.configure(text = "True")
    else:
        label.configure(text = "False")

# create root window
root = tk.Tk()

# root window title and dimension
root.title("Legal Description Comparer")
root.geometry('600x400')

# define input text windows
box1 = scrolledtext.ScrolledText(root, wrap = tk.WORD, height = 15, width = 35, font = ("Times New Roman", 11))
box2 = scrolledtext.ScrolledText(root, wrap = tk.WORD, height = 15, width = 35, font = ("Times New Roman", 11))

# place box1 and 2 on the window
box1.pack(side=tk.LEFT, padx=10, pady=10)
box2.pack(side=tk.RIGHT, padx=10, pady=10)

# define "compare" button
button = tk.Button(root, width=20, text = "Compare", command = compare)
button.pack(pady=5)

# define output label
label = tk.Label(root, text="")
label.pack()

# execute Tkinter
root.mainloop()