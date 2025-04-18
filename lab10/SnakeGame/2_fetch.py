def get_latest_level(user_id):
    conn = psycopg2.connect(database="your_db", user="your_user", password="your_pass", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT level FROM user_scores WHERE user_id=%s ORDER BY created_at DESC LIMIT 1", (user_id,))
    level = cur.fetchone()
    conn.close()
    return level[0] if level else 1
