from lib.db.connection import get_connection

def seed():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(open("lib/db/schema.sql").read())
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Alice",))
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Bob",))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Today", "Technology"))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Weekly", "Health"))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("AI Revolution", 1, 1))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", ("Wellness Tips", 2, 2))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed()