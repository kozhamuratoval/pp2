def insert_from_console():
    conn = psycopg2.connect(database="your_db", user="your_user", password="your_pass", host="localhost", port="5432")
    cur = conn.cursor()
    name = input("Enter username: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()