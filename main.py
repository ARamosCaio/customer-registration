from tkinter import *


root = Tk()

class Application():
    def __init__(self):
        self.root = root 
        self.screen_config()
        self.screen_frames()
        self.top_frame_widgets()
        root.mainloop()

    def screen_config(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background="#1e3743")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)
    
     
    def screen_frames(self):
        self.top_frame = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3)
        self.top_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.bottom_frame = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3)
        self.bottom_frame.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    def top_frame_widgets(self):
        self.clear_btn = Button(self.top_frame, text="Limpar")
        self.clear_btn.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        self.search_btn = Button(self.top_frame, text="Procurar")
        self.search_btn.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.new_btn = Button(self.top_frame, text="Novo")
        self.new_btn.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.change_btn = Button(self.top_frame, text="Alterar")
        self.change_btn.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.delete_btn = Button(self.top_frame, text="Apagar")
        self.delete_btn.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)


        self.code_label = Label(self.top_frame, text="Código")
        self.code_label.place(relx=0.05, rely=0.05)

        self.code_insert = Entry(self.top_frame)
        self.code_insert.place(relx=0.05, rely=0.15, relwidth=0.08, relheight=0.1)

        
        self.name_label = Label(self.top_frame, text="Nome")
        self.name_label.place(relx=0.05, rely=0.35)

        self.name_insert = Entry(self.top_frame)
        self.name_insert.place(relx=0.05, rely=0.45, relwidth=0.8, relheight=0.1)

Application()