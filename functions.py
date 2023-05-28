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
            codes INTEGER PRIMARY KEY,
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

        self.cursor.execute(""" DELETE from customers WHERE codes = ? """, str(self.code))
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