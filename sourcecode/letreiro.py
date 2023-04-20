import tkinter as tk

class Letreiro(tk.Canvas):
    def __init__(self, master, text, width, height, speed):
        super().__init__(master, width=width, height=height, highlightthickness=0, bg="black")
        self.speed = speed
        self.text = self.create_text(0, height/2, text=text, font=("Arial", 40), fill="red", anchor="w")
        self.text_width = self.bbox(self.text)[2] - self.bbox(self.text)[0]
        self.pos = width
        
    def move(self):
        dx = self.speed / 60 
        self.pos -= dx
        if self.pos < -self.text_width:
            self.pos = self.winfo_width()
        self.coords(self.text, self.pos, self.winfo_height()/2)
        self.after(16, self.move)

root = tk.Tk()
root.title("Letreiro by Inacio Buemo")
root.configure(bg="black")

frase_var = tk.StringVar()
frase_entry = tk.Entry(root, textvariable=frase_var, font=("Arial", 20), width=30, bg="black", fg="red")
frase_entry.pack(pady=10)
frase_entry.focus_set()

def start_letreiro():
    frase_entry.pack_forget()
    start_button.pack_forget()

    frase = frase_var.get()
    letreiro = Letreiro(root, frase, root.winfo_width(), root.winfo_height(), 300)
    letreiro.pack()
    letreiro.move()

start_button = tk.Button(root, text="poggers", font=("Arial", 20), command=start_letreiro, bg="black", fg="red")
start_button.pack(pady=10)

root.mainloop()
