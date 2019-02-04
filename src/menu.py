import tkinter as tk
from PIL import ImageTk, Image


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

    img = ImageTk.PhotoImage(Image.open("sprites/spikes.png"))
    panel = tk.Label(root, image=img)
    panel.pack()

    choise = tk.IntVar()

    red_rbutton = tk.Radiobutton(root, text="Red", value=0, variable=choise)
    red_rbutton.pack()

    blue_rbutton = tk.Radiobutton(root, text="Blue", value=1, variable=choise)
    blue_rbutton.pack()

    confirm_button = tk.Button(root, text="confirm", command=lambda: root.destroy()).pack()
    win = Window(root=root)

    root.mainloop()
    return "red" if choise.get() == 0 else "blue"
