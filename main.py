from tkinter import *


root = Tk()

class Application():
    def __init__(self):
        self.root = root 
        self.screen_config()
        self.screen_frames()
        root.mainloop()

    def screen_config(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background="#1e3743")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)
    
     
    def screen_frames(self):
        self.top_frame = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3)
        self.top_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.bottom_frame = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3)
        self.bottom_frame.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

Application()