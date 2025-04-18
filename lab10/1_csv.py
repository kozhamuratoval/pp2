import psycopg2
import csv

def insert_from_csv(filename):
    conn = psycopg2.connect(database="your_db", user="your_user", password="your_pass", host="localhost", port="5432")
    cur = conn.cursor()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    conn.close()