from tkinter import *
from tkinter import ttk
import sqlite3

import functions

root = Tk()


class Application(Functions):
    def __init__(self):
        self.root = root 
        self.screen_config()
        self.screen_frames()
        self.top_frame_widgets()
        self.bottom_frame_widgets()
        self.db_create()
        self.select_customer()
        self.menu()
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


        self.clear_btn = Button(self.top_frame, text="Limpar", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), activebackground='#108ecb', activeforeground='white', command=self.clear)
        self.clear_btn.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        self.search_btn = Button(self.top_frame, text="Procurar", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), activebackground='#108ecb', activeforeground='white', command=self.search_customer)
        self.search_btn.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.new_btn = Button(self.top_frame, text="Novo", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), activebackground='#108ecb', activeforeground='white', command=self.add_customer)
        self.new_btn.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.change_btn = Button(self.top_frame, text="Alterar", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), activebackground='#108ecb', activeforeground='white', command=self.change_customer)
        self.change_btn.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.delete_btn = Button(self.top_frame, text="Apagar", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), activebackground='#108ecb', activeforeground='white', command=self.delete_customer)
        self.delete_btn.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)


        self.code_label = Label(self.top_frame, text="Código", bg="#dfe3ee", fg="#107db2")
        self.code_label.place(relx=0.05, rely=0.05)

        self.code_insert = Entry(self.top_frame)
        self.code_insert.place(relx=0.05, rely=0.15, relwidth=0.08, relheight=0.1)

        
        self.name_label = Label(self.top_frame, text="Nome", bg="#dfe3ee",fg="#107db2")
        self.name_label.place(relx=0.05, rely=0.35)

        self.name_insert = Entry(self.top_frame)
        self.name_insert.place(relx=0.05, rely=0.45, relwidth=0.8, relheight=0.1)


        self.phone_label = Label(self.top_frame, text="Telefone", bg="#dfe3ee", fg="#107db2")
        self.phone_label.place(relx=0.05, rely=0.6)

        self.phone_insert = Entry(self.top_frame)
        self.phone_insert.place(relx=0.05, rely=0.7, relwidth=0.4, relheight=0.1)


        self.city_label = Label(self.top_frame, text="Cidade", bg="#dfe3ee", fg="#107db2")
        self.city_label.place(relx=0.5, rely=0.6)

        self.city_insert = Entry(self.top_frame)
        self.city_insert.place(relx=0.5, rely=0.7, relwidth=0.4, relheight=0.1)

    def bottom_frame_widgets(self):

        self.list = ttk.Treeview(self.bottom_frame, height=3, columns=("col1", "col2", "col3", "col4"))
        self.list.heading("#0")
        self.list.heading("#1", text="Código")
        self.list.heading("#2", text="Nome")
        self.list.heading("#3", text="Telefone")
        self.list.heading("#4", text="Cidade")
        
        self.list.column("#0", width=1)
        self.list.column("#1", width=50)
        self.list.column("#2", width=200)
        self.list.column("#3", width=125)
        self.list.column("#4", width=125)

        self.list.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollbar = Scrollbar(self.bottom_frame, orient="vertical")
        self.list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.list.bind("<Double-1>", self.double_click)

    def menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu = menu_bar)
        first_menu = Menu(menu_bar)
        second_menu = Menu(menu_bar)

        def quit():
            self.root.destroy()
        
        menu_bar.add_cascade(label = "Opções", menu = first_menu)
        menu_bar.add_cascade(label = "Sobre", menu = second_menu)

        first_menu.add_command(label="Sair", command=quit)
        second_menu.add_command(label="Limpar", command=self.clear)

Application()