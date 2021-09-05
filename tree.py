from tkinter import ttk
import tkinter as tk
import sqlite3


def connect():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS profile(
        id INTEGER PRIMARY KEY,
        First TEXT,
        Surname TEXT)""")
    conn.commit()
    conn.close()


def View():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profile")
    tree.delete(*tree.get_children())
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


def View_entry_get():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    a = cur.execute(f"""SELECT * FROM profile WHERE surname="Falcon" """)
    # a = cur.execute(f"""SELECT * FROM profile WHERE surname="" """)
    print(a)
    tree.delete(*tree.get_children())
    rows = cur.fetchall()
    print(rows)
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


def delete_all_rows(table_name):
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    "deletes all rows in the table passed as arguments"
    conn.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()


data = """Gio,Gatto
Sam,Falcon
Ira,Conda
""".splitlines()


# data = ["Gio, Gatto", ...]

def add_data():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    delete_all_rows("profile")
    for n, d in enumerate(data):
        name, surname = d.split(",")
        cur.execute(f"""INSERT INTO profile (id, first, surname) VALUES ({n}, "{name}", "{surname}")""")

    # cur.execute("""INSERT INTO profile (id, first, surname) VALUES (1, "gio", "gatto")""")
    # cur.execute("""INSERT INTO profile (id, first, surname) VALUES (2, "Sam", "Falcon")""")
    conn.commit()
    conn.close()

connect()  #  this to create the db

add_data()
root = tk.Tk()
root.geometry("800x400")

tree= ttk.Treeview(root, column=("column1", "column2", "column3"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="SURNAME")
tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()

b3 = tk.Button(text="view query Falcon", command=View_entry_get)
b3.pack()



root.mainloop()