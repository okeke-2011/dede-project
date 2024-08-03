import tkinter as tk

def tk_test():
    root = tk.Tk()

    root.geometry("500x500")
    root.title("Engraved Plain")

    buttonframe = tk.Frame(root)
    for i in range(5):
        buttonframe.columnconfigure(i, weight=1)

    for i in range(5):
        for j in range(5):
            num = 5 * i + j + 1
            btn = tk.Button(buttonframe, text="⬜️", font=('Arial', 18), height=2, width=2)
            btn.grid(row=i, column=j, sticky=tk.W+tk.E)

    buttonframe.pack(padx=20, pady=100)


    root.mainloop()

if __name__ == "__main__":
    tk_test()