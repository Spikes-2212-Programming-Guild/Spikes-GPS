import tkinter as tk


class Window(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, master=root)
        self.master = root
        self.pack(fill=tk.BOTH, expand=1)


def draw_menu():
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Spikes GPU")
    root.iconbitmap("sprites/Logo.ico")

    choice = tk.IntVar()

    red_button = tk.Radiobutton(root, text="Red", value=0, variable=choice)
    red_button.pack()

    blue_button = tk.Radiobutton(root, text="Blue", value=1, variable=choice)
    blue_button.pack()

    confirm_button = tk.Button(root, text="confirm", command=lambda: root.destroy()).pack()
    win = Window(root=root)

    root.mainloop()
    return "red" if choice.get() == 0 else "blue"
