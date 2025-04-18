def update_phonebook(old_username, new_username=None, new_phone=None):
    conn = psycopg2.connect(database="your_db", user="your_user", password="your_pass", host="localhost", port="5432")
    cur = conn.cursor()
    if new_username:
        cur.execute("UPDATE phonebook SET username=%s WHERE username=%s", (new_username, old_username))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE username=%s", (new_phone, new_username or old_username))
    conn.commit()
    conn.close()