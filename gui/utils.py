import psycopg2  # type: ignore
from datetime import datetime, timedelta

class AnalizedPost:
    def __init__(self, url, content, compound, negative, neutral, positive, created):
        self.url = url;
        self.content = content;
        self.compound = compound;
        self.negative = negative;
        self.neutral = neutral;
        self.positive = positive;
        self.created = created;


def get_analized_from_last_mins(mins=5):
    conn = psycopg2.connect(database="analized_data", user="admin", password="root", host="postgres_db", port=5432)

    cursor = conn.cursor()
    
    # Execute the SQL query
    cursor.execute('''
        SELECT * FROM analized
        WHERE created >= NOW() - INTERVAL '2 minutes';
    ''', mins)
    
    # Fetch and print the results
    rows = cursor.fetchall()
    records = [
        AnalizedPost(url=row[1],
                     content=row[2],
                     compound=row[3],
                     negative=row[4],
                     neutral=row[5],
                     positive=row[6],
                     created=row[7]
        )
        for row in rows
    ]

    cursor.close()
    conn.close()
    return records;