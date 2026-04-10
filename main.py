import tkinter as tk
from tkinter.font import Font
from random import choice


word = vzor = None

with open("db.py", "r") as file:
    db = eval(file.read())

def check_word(i):
    buttons[i]["bg"] = "red"
    buttons[i]["activebackground"] = "red"
    for b in buttons:
        if b["text"] == db[word][vzor]:
            b["bg"] = "green"
            b["activebackground"] = "green"

def next_word():
    global word, vzor
    word = choice(tuple(db.keys()))
    vzor = choice(tuple(db[word].keys()))

    label["text"] = f"{word} {vzor}"
    l = list(set(db[word].values()))
    l.remove(db[word][vzor])
    for b in buttons:
        b["text"] = choice(l)
        l.remove(b["text"])
        b["bg"] = "white"
        b["activebackground"] = "white"
    button = choice(buttons)
    button["text"] = db[word][vzor]

root = tk.Tk()
root.geometry("700x500")

font = Font(size=32)

frame = tk.Frame(root, width=500, height=700)

label = tk.Label(frame, font=font, border=32)

button0 = tk.Button(frame, command=lambda: check_word(0), font=font)
button1 = tk.Button(frame, command=lambda: check_word(1), font=font)
button2 = tk.Button(frame, command=lambda: check_word(2), font=font)
button3 = tk.Button(frame, command=lambda: check_word(3), font=font)
buttonn = tk.Button(frame, command=next_word, text="next", font=font)
buttons = [button0, button1, button2, button3]

frame.pack()
label.pack()
button0.pack()
button1.pack()
button2.pack()
button3.pack()
buttonn.pack()

root.bind("<Escape>", lambda x: root.destroy())

if __name__ == "__main__":
    next_word()
    root.mainloop()
