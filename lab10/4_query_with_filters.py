def query_phonebook(filter_value):
    conn = psycopg2.connect(database="your_db", user="your_user", password="your_pass", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s OR phone ILIKE %s", (f'%{filter_value}%', f'%{filter_value}%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    