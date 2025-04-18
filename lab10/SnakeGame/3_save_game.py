def save_score(user_id, score, level, state=None):
    conn = psycopg2.connect(database="your_db", user="your_user", password="your_pass", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO user_scores (user_id, score, level, saved_state) VALUES (%s, %s, %s, %s)",
                (user_id, score, level, psycopg2.Binary(state) if state else None))
    conn.commit()
    conn.close()
    