from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()

class Functions():
    def clear(self):
        self.code_insert.delete(0, END)
        self.name_insert.delete(0, END)
        self.phone_insert.delete(0, END)
        self.city_insert.delete(0, END)
    
    def db_connect(self):
        self.connect = sqlite3.connect("customer_register.db")
        self.cursor = self.connect.cursor()
    
    def db_disc(self):
        self.connect.close()
    
    def db_create(self):

        self.db_connect(); print("Conectando ao BD")

        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS customers (
            codes  INTEGER PRIMARY KEY,
            customer_name CHAR(40) NOT NULL,
            customer_phone INTEGER(20),
            customer_city CHAR(40)
            );
        """)

        self.connect.commit(); print("BD criado")
        self.db_disc()
    
    def add_customer(self):
        
        self.code = self.code_insert.get()
        self.name = self.name_insert.get()
        self.phone = self.phone_insert.get()
        self.city = self.city_insert.get()

        self.db_connect()
        
        self.cursor.execute(""" INSERT INTO customers (customer_name, customer_phone, customer_city) VALUES (?, ?, ?)""", (self.name, self.phone, self.city))

        self.connect.commit()
        self.db_disc
        self.select_customer()
        self.clear()
        
    def select_customer(self):
        self.list.delete(*self.list.get_children())
        self.db_connect()
        list = self.cursor.execute(""" SELECT codes, customer_name, customer_phone, customer_city FROM customers ORDER BY customer_name ASC; """)

        for i in list:
            self.list.insert("", END, values=i)
        
        self.db_disc()

    def double_click(self, event):

        self.clear()
        self.list.selection()

        for i in self.list.selection():
            col1, col2, col3, col4 = self.list.item(i, "values")
            self.code_insert.insert(END, col1)
            self.name_insert.insert(END, col2)
            self.phone_insert.insert(END, col3)
            self.city_insert.insert(END, col4)

    def delete_customer(self):

        self.code = self.code_insert.get()
        self.name = self.name_insert.get()
        self.phone = self.phone_insert.get()
        self.city = self.city_insert.get()

        self.db_connect()

        self.cursor.execute(""" DELETE from customers WHERE codes = ? """, (self.code))
        self.connect.commit()

        self.db_disc()

        self.clear()
        self.select_customer()

    def change_customer(self):

        self.code = self.code_insert.get()
        self.name = self.name_insert.get()
        self.phone = self.phone_insert.get()
        self.city = self.city_insert.get()

        self.db_connect()
        self.cursor.execute("""UPDATE customers SET customer_name = ?, customer_phone = ?, customer_city = ? WHERE codes = ? """, (self.name, self.phone, self.city, self.code))
        self.connect.commit()
        self.db_disc()
        self.select_customer()
        self.clear()

    def search_customer(self):
        self.db_connect()
        self.list.delete(*self.list.get_children())
        self.name_insert.insert(END, '%')
        name = self.name_insert.get()
        self.cursor.execute("""SELECT codes, customer_name, customer_phone, customer_city FROM customers WHERE customer_name LIKE '%s' ORDER BY customer_name ASC""" % name)
        search_name = self.cursor.fetchall()
        for i in search_name:
            self.list.insert("", END, values=i)
        self.clear()
        self.db_disc()
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

        self.canvas = Canvas(self.top_frame, bd=0, bg='#1e3743', highlightbackground = 'gray', highlightthickness = 2)
        self.canvas.place(relx=0.195, rely=0.09, relwidth=0.21, relheight=0.18)

        self.clear_btn = Button(self.top_frame, text="Limpar", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), command=self.clear)
        self.clear_btn.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        self.search_btn = Button(self.top_frame, text="Procurar", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), command=self.search_customer)
        self.search_btn.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.new_btn = Button(self.top_frame, text="Novo", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), command=self.add_customer)
        self.new_btn.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.change_btn = Button(self.top_frame, text="Alterar", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), command=self.change_customer)
        self.change_btn.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.delete_btn = Button(self.top_frame, text="Apagar", bd=2, bg="#107db2", foreground="white", font=("verdana", 9, "bold"), command=self.delete_customer)
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
        self.list.heading("#0", text="")
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