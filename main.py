import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
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

def new_file(window, text_field):
    global file_name
    file_name = None
    text_field.delete(1.0, tk.END)
    window.title("Welcome to Simple.txt")

def update_font_size(spinbox, text_field, my_font):
    try:
        font_size = spinbox.get()
        my_font.configure(size=font_size)
        text_field.configure(my_font)
    except TypeError as e:
        pass
#the functionality works even with the TypeError, so this keeps the terminal from filling with errors.

def update_font(combobox, text_field, my_font):
    try:
        font_style = combobox.get()
        my_font.configure(family=font_style)
        text_field.configure(my_font)
    except TypeError as e:
        pass
#the functionality works even with the TypeError, so this keeps the terminal from filling with errors.
    

def main():
    window = tk.Tk()
    window.title("Welcome to Simple.txt")
    window.geometry("1000x700")
    frame = ttk.Frame(window, padding="3 3 12 12")
    frame.grid(column=0, row=0, sticky=("nsew"))
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=1)

    my_font = font.Font(family="default", size=12)
    text_var = StringVar(window)
    text_var.set("12")
    text_field = Text(window, background="black", fg="white", insertbackground="white", wrap=WORD)
    text_field.grid(column=1, row=0, sticky="nsew")
    text_field.configure(font=my_font)

    save_button = ttk.Button(frame, text="Save", command=lambda: save_file(window, text_field))
    save_button.grid(column=0, row=0, sticky=("ew"))

    open_button = ttk.Button(frame, text="Open", command=lambda: open_file(window, text_field))
    open_button.grid(column=0, row=1, sticky=("ew"))

    new_button = ttk.Button(frame, text="New", command= lambda: new_file(window, text_field))
    new_button.grid(column=0, row=2, sticky=("ew"))

    size_label = ttk.Label(frame, text="Font Size:")
    size_label.grid(column=0, row=3, sticky=("ew"))

    font_size_selector = ttk.Spinbox(frame, from_=0, to=100, width=2, textvariable=text_var)
    font_size_selector.grid(column=0, row=4, sticky=("ew"))
    font_size_selector.config(command=lambda: update_font_size(font_size_selector, text_field, my_font))

    font_label = ttk.Label(frame, text="Font:")
    font_label.grid(column=0, row=5, sticky=("ew"))

    font_selector = ttk.Combobox(frame)
    font_selector["values"] = (list(set(font.families()))) #This is kinda ugly, but it works.
    font_selector.grid(column=0, row=6, sticky=("ew"))

    window.bind("<Control-s>", lambda x: save_file(window, text_field))
    window.bind("<Control-o>", lambda x: open_file(window, text_field))
    window.bind("<Control-n>", lambda x: new_file(window, text_field))
    font_size_selector.bind("<Return>", lambda x: update_font_size(font_size_selector, text_field, my_font))
    font_selector.bind("<<ComboboxSelected>>", lambda x: update_font(font_selector, text_field, my_font))

    window.mainloop()

main()