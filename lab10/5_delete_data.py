def delete_entry(value):
    conn = psycopg2.connect(database="your_db", user="your_user", password="your_pass", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE username=%s OR phone=%s", (value, value))
    conn.commit()
    conn.close()