import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

file_name = None

def open_file(window, text_field):
    global file_name
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return
    text_field.delete(1.0, tk.END)
    with open(file_path, "r") as f:
        content = f.read()
        text_field.insert(tk.END, content)
    window.title(f"Open File: {os.path.basename(file_path)}")
    file_name = os.path.basename(file_path)

def save_file(window, text_field):
    global file_name
    if not file_name:
        file_path = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        with open(file_path, "w") as f:
            content = text_field.get(1.0, tk.END)
            f.write(content)
        file_name = os.path.basename(file_path)
        window.title(f"Open File: {os.path.basename(file_path)}")
    else:
        with open(file_name, "w") as f:
            content = text_field.get(1.0, tk.END)
            f.write(content)
    

def main():
    window = tk.Tk()
    window.title("Welcome to Simple.txt")
    window.geometry("1000x700")
    frame = ttk.Frame(window, padding="3 3 12 12")
    frame.grid(column=0, row=0, sticky=("nsew"))
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)

    text_field = Text(window, background="black", fg="white", insertbackground="white", wrap=WORD)
    text_field.grid(column=1, row=0, sticky="nsew")

    save_button = ttk.Button(frame, text="Save", command=lambda: save_file(window, text_field))
    save_button.grid(column=0, row=0, sticky=("ew"))
    open_button = ttk.Button(frame, text="Open", command=lambda: open_file(window, text_field))
    open_button.grid(column=0, row=1, sticky=("ew"))

    window.bind("<Control-s>", lambda x: save_file(window, text_field))
    window.bind("<Control-o>", lambda x: open_file(window, text_field))

    window.mainloop()

main()