from flask import Flask, request, jsonify  # type: ignore
from utils import fetch_content, setup_db
from datetime import datetime
import psycopg2  # type: ignore


def save_in_db(tuples):
    # Connect to SQLite database (or create one)
    conn = psycopg2.connect(database="scraped_data", user="admin", password="root", host="postgres_db", port=5432)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    print('inserting into posts')
    cursor.executemany('INSERT INTO posts (url, content, created) VALUES (%s, %s, %s);', tuples)

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

app = Flask(__name__)

@app.route('/submit-urls', methods=['POST'])
def submit_urls():
    urls = request.json.get('urls', [])
    
    # scrape given urls
    for url in urls:
        tuples = []
        parsed_data = fetch_content(url)
        for text in parsed_data:
            tuples.append((url, text, str(datetime.now())))

        save_in_db(tuples)
    
    print(f"Received URLs: {urls}")
    return jsonify({"status": "success", "message": f"Received {len(urls)} URLs"})

@app.route('/print', methods=['GET'])
def print_db():
    conn = psycopg2.connect(database="scraped_data", user="admin", password="root", host="postgres_db", port=5432)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM posts;')
    rows = []
    for row in cursor:
        rows.append(row)
    
    cursor.close()
    conn.close()
    
    return jsonify({"result": f"{rows}"})


if __name__ == '__main__':
    setup_db()
    app.run(host='0.0.0.0', port=5000)
