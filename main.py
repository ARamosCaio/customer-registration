from tkinter import *


root = Tk()

class Application():
    def __init__(self):
        self.root = root 
        self.screen_config()
        self.screen_frames()
        self.main_buttons()
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
    
    def main_buttons(self):
        self.clear_btn = Button(self.top_frame, text="Limpar")
        self.clear_btn.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.15)
        
        self.search_btn = Button(self.top_frame, text="Procurar")
        self.search_btn.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.15)

        self.new_btn = Button(self.top_frame, text="Novo")
        self.new_btn.place(relx=0.45, rely=0.1, relwidth=0.1, relheight=0.15)

        self.change_btn = Button(self.top_frame, text="Alterar")
        self.change_btn.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.15)

        self.delete_btn = Button(self.top_frame, text="Apagar")
        self.delete_btn.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.15)

        

Application()