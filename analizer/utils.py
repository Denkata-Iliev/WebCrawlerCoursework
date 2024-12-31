import psycopg2  #type: ignore
from datetime import datetime, timedelta


def setup_db():
    conn = psycopg2.connect(database="analized_data", user="admin", password="root", host="postgres_db", port=5432)

    cursor = conn.cursor()

    # Create a table for storing analized data
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analized (
        id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        url TEXT,
        content TEXT,
        compound REAL,
        negative REAL,
        neutral REAL,
        positive REAL,
        created TIMESTAMP
    );
    ''')

    conn.commit()
    conn.close()


class Post:
    def __init__(self, url, content, created):
        self.url = url;
        self.content = content;
        self.created = created;


def get_all_last_mins(mins=5):
    conn = psycopg2.connect(database="scraped_data", user="admin", password="root", host="postgres_db", port=5432)

    cursor = conn.cursor()

    threshold_time = datetime.now() - timedelta(minutes=mins)
    
    # Execute the SQL query
    cursor.execute('''
        SELECT * FROM posts
        WHERE created >= %s;
    ''', (threshold_time,))
    
    # Fetch and print the results
    # rows = cursor.fetchall()
    records = []
    for row in cursor:
        records.append(
            Post(
                url=row[1],
                content=row[2],
                created=row[3]
            )
        )

    cursor.close()
    conn.close()
    return records;

def save_in_db(analizedRecord):
    conn = psycopg2.connect(database="analized_data", user="admin", password="root", host="postgres_db", port=5432)

    cursor = conn.cursor()

    insert_query = '''
        INSERT INTO analized (url, content, compound, negative, neutral, positive, created)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    '''
    
    cursor.execute(insert_query, (
        analizedRecord.url,
        analizedRecord.content,
        analizedRecord.compound,
        analizedRecord.negative,
        analizedRecord.neutral,
        analizedRecord.positive,
        datetime.now()
    ))

    conn.commit()
    cursor.close()
    conn.close()
