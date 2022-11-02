from time import sleep
import tkinter as tk
from types import NoneType
import typer
from threading import Thread
from keyboard import press, press_and_release, release

root = tk.Tk()

root.title("Auto Typer")
root.geometry('350x400')
root.resizable(False, False)

first_line = tk.Frame()
second_line = tk.Frame()
third_line = tk.Frame()
fourth_line = tk.Frame()
fifth_line = tk.Frame()
sixth_line = tk.Frame()
seventh_line = tk.Frame()

text = ""
edited_label = tk.Text(sixth_line, width=40, height=5)

def capture(repeat, reverse, begins, contain, nospace):
    global text
    global edited_label

    text = typer.capture(repeat, reverse, contain, begins, nospace)
    
    if(text != NoneType and text != None):
        for widget in sixth_line.winfo_children():
            widget.destroy()

        edited_label = tk.Text(sixth_line, width=40, height=5)
        edited_label.insert(tk.END, text)
        edited_label.pack(side=tk.LEFT)
    else:
        for widget in sixth_line.winfo_children():
            widget.destroy()

        none_label = tk.Label(sixth_line, text="No text detected")
        none_label.pack(side=tk.LEFT)

def start():
    with open("blocked_keys.txt", "r") as blocked_keys_txt:
        blocked_keys = blocked_keys_txt.read()

    if(text != NoneType and text != None):
        edited_text = edited_label.get("1.0",tk.END)
        edited_text = edited_text[:-1]
        typer.start_typing(edited_text, blocked_keys)

def open_settings():
    def on_closing():
        with open("blocked_keys.txt", "w") as blocked_keys_txt:
            blocked_keys_txt.write(blocked_keys.get("1.0",tk.END)[:-1])
        
        settings_window.destroy()
    
    settings_window = tk.Toplevel(root)
    settings_window.grab_set()
    settings_window.title("Auto Typer Settings")
    settings_window.geometry('350x100')
    settings_window.resizable(False, False)
    settings_window.protocol("WM_DELETE_WINDOW", on_closing)

    blocked_text = tk.Label(settings_window, text="Additional blocked keys: ")
    blocked_text.pack(side=tk.LEFT)
    blocked_keys = tk.Text(settings_window, height=1)
    blocked_keys.pack(side=tk.LEFT)

    with open("blocked_keys.txt", "r") as blocked_keys_txt:
        blocked_keys.insert(tk.END, blocked_keys_txt.read())
        


menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)

file_menu.add_command(
    label='Settings',
    command=open_settings,
)
file_menu.add_command(
    label='Exit',
    command=root.destroy,
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)


repeat_label = tk.Label(first_line, text="Repeat: ")
repeat_label.pack(side=tk.LEFT)

repeat_value = tk.StringVar(value=0)
repeat_select = tk.Spinbox(first_line, from_=1, to=10, textvariable=repeat_value)
repeat_select.pack(side=tk.LEFT)


reverse_label = tk.Label(second_line, text="Reverse: ")
reverse_label.pack(side=tk.LEFT)

reverse_value = tk.BooleanVar()
reverse_select = tk.Checkbutton(second_line, variable=reverse_value, onvalue=True, offvalue=False)
reverse_select.pack(side=tk.LEFT)


nospace_label = tk.Label(second_line, text="No spaces: ")
nospace_label.pack(side=tk.LEFT)

nospace_value = tk.BooleanVar()
nospace_select = tk.Checkbutton(second_line, variable=nospace_value, onvalue=True, offvalue=False)
nospace_select.pack(side=tk.LEFT)


letter_value = tk.IntVar(value=0)
begins_value = tk.StringVar()
contains_value = tk.StringVar()
def select_option():
    if letter_value.get() == 0:
        for widget in fourth_line.winfo_children():
            widget.destroy()
        begins_value.set("")
        contains_value.set("")
    elif letter_value.get() == 1:
        for widget in fourth_line.winfo_children():
            widget.destroy()
        contains_value.set("")
            
        begins_label = tk.Label(fourth_line, text="Begins with: ")
        begins_label.pack(side=tk.LEFT)

        begins_select = tk.Entry(fourth_line, textvariable=begins_value)
        begins_select.pack(side=tk.LEFT)
    elif letter_value.get() == 2:
        for widget in fourth_line.winfo_children():
            widget.destroy()
        begins_value.set("")

        contains_label = tk.Label(fourth_line, text="Contains: ")
        contains_label.pack(side=tk.LEFT)

        contains_select = tk.Entry(fourth_line, textvariable=contains_value)
        contains_select.pack(side=tk.LEFT)
letter_select = tk.Radiobutton(third_line, text="Begins with", variable=letter_value, command=select_option,value=1)
letter_select.pack(side=tk.LEFT)
letter_select = tk.Radiobutton(third_line, text="Contains", variable=letter_value, command=select_option,value=2)
letter_select.pack(side=tk.LEFT)
letter_select = tk.Radiobutton(third_line, text="None", variable=letter_value, command=select_option,value=0)
letter_select.pack(side=tk.LEFT)

capture_button = tk.Button(fifth_line, text ="Capture", command = lambda: capture(int(repeat_value.get()), bool(reverse_value.get()), begins_value.get(), contains_value.get(), bool(nospace_value.get())))
capture_button.pack(side=tk.LEFT)

start_button = tk.Button(seventh_line, text ="Start", command = lambda: start())
start_button.pack(side=tk.LEFT)


first_line.pack()
second_line.pack()
third_line.pack()
fourth_line.pack()
fifth_line.pack()
sixth_line.pack()
seventh_line.pack()



root.mainloop()
