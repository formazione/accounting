import sqlite3 as lite

'''
Create cursor...
cur = conn.cursor()

Create table
cur.execute("""CREATE TABLE IF NOT EXISTS profile(
    id INTEGER PRIMARY KEY,
    First TEXT,
    Surname TEXT)""")


Insert data into table
================================
001
================================

<p>
Let's create a db and let's also close it.
We also set the cursor, that is needed to 
start making thing with the data.
</p>

import sqlite3 as lite


def start(fname):
    conn = lite.connect(fname)
    cur = conn.cursor()
    conn.close()

start("db2.db")

=====================================
002.
====================

We create a function to add a table

def add_table(cur, name, fields):
    tablename = "profile"
    command = "CREATE TABLE IF NOT EXISTS"
    # converts tuple of fields to string for the execute command
    fields = ",".join(fields)
    cur.execute(f"{command} {name} ({fields})")

# ==================
# 003
# ==========

let's use the function to add some fields


    # ============================ debug
    add_table(cur,
        "profile", # name of the table
        (   # fields for data
            "id INTEGER PRIMARY KEY",
            "First TEXT",
            "Surname TEXT"))
    # debug ============================

    =====
    004
    =====
    now we put some example data


'''
def add_table(cur, name, fields):
    tablename = "profile"
    command = "CREATE TABLE IF NOT EXISTS"
    # converts tuple of fields to string for the execute command
    fields = ",".join(fields)
    cur.execute(f"{command} {name} ({fields})")


def add_data(cur, data):
    for n, d in enumerate(data):
        name, surname = d
        # Inserting into the fields the values into the list of tuples with data (name, surname)
        cur.execute(f"""INSERT INTO profile (id, first, surname) VALUES ({n}, "{name}", "{surname}")""")



def start(fname):
    global fields

    # OPEND or CREATE DATABASE and creating a cursor
    conn = lite.connect(fname)
    cur = conn.cursor()
    # This function add table passing name and fields for data


    # ============= FIELDS OF THE TABLE
    add_table(cur,
        "profile", # name of the table
        (   # fields for data
            "id INTEGER PRIMARY KEY",
            "First TEXT",
            "Surname TEXT"))


    # ==================================
    # Inserting data according to FIELDS
    add_data(cur,
        [("Gio","Gatto"),
        ("Sam","Falcon"),
        ("Ira", "Conda")])

    # ==================================
    # Quering the data - Selecting all the data
    cur.execute("SELECT * FROM profile")
    
    # ====================================
    # showing the data  - getting a list of the rows
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("I passed the rows")

    conn.close()

start("db2.db")