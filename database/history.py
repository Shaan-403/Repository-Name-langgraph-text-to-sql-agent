import sqlite3

conn = sqlite3.connect(
    "history.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS query_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    sql_query TEXT,
    answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


def save_query(question, sql, answer):

    cursor.execute(
        """
        INSERT INTO query_history
        (
            question,
            sql_query,
            answer
        )
        VALUES (?, ?, ?)
        """,
        (
            question,
            sql,
            answer
        )
    )

    conn.commit()


def get_recent_queries(limit=20):

    cursor.execute(
        """
        SELECT
            question,
            created_at
        FROM query_history
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    return cursor.fetchall()

def get_recent_queries(limit=20):

    cursor.execute("""
        SELECT
            question,
            sql_query,
            created_at
        FROM query_history
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    return cursor.fetchall()