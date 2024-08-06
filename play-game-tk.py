import tkinter as tk
from tkmacosx import Button

def tk_test():
    root = tk.Tk()

    root.geometry("500x500")
    root.title("Engraved Plain")

    buttonframe = tk.Frame(root)
    for i in range(5):
        buttonframe.columnconfigure(i, weight=1)

    buttons = {}
    for i in range(5):
        for j in range(5):
            btn = Button(buttonframe, text="", font=('Arial', 18), height=60, width=60, command=lambda i=i, j=j: onClick(buttons, i, j))
            btn.grid(row=i, column=j, sticky=tk.W+tk.E)
            buttons[(i, j)] = btn

    buttonframe.pack(padx=20, pady=80)

    root.mainloop()

def onClick(buttons, i, j):
    btn = buttons[(i, j)]
    btn.config(text="🟩")
    btn.config(bg="#c1ffa7")

# #c1ffa7 - green
# #ff9580 - red

if __name__ == "__main__":
    tk_test()