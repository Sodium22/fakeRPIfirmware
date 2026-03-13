import os
import tkinter as tk
from tkinter import *
from glob import glob
from pathlib import Path

"""

!!!!!!!!!!!!!!!!!!!!!!!!

Change from TK to PYQT-6

!!!!!!!!!!!!!!!!!!!!!!!!

"""


main = Path(__file__).parent
scripts = main / "Scripts"
b = {}

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack(fill = "both", expand = True)
input1 = tk.Entry(root)
input1.pack(fill = "both", expand = True)

"""root.title("GfG")                           #Creates a second window
top = Toplevel()
tk.Label(top, text = "TEST").pack()
tk.Button(top, text = "TEST").pack()"""

for file in scripts.rglob("*.txt"):
    b[file.stem] = file

    listbox.insert(tk.END, file.stem)


def on_select(event):
    selection = listbox.get(listbox.curselection())
    #test = selection + ".txt"

    file_path = b[selection]
    excode = file_path.read_text()
    exec(excode)


listbox.bind('<<ListboxSelect>>', on_select)

root.mainloop()

