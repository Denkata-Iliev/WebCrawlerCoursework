from flask import Flask, request, jsonify  # type: ignore
from utils import fetch_content, setup_db
from datetime import datetime
import requests  # type: ignore
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
    
    response = requests.post(
        'http://analizer-app:5001/new-data-ready',
        json={"message": "New data available"}
    )

    if response.status_code == 200:
        print('Notified analizer successfully!')
    
    return jsonify({"status": "success", "message": f"Received {len(urls)} URLs"})

if __name__ == '__main__':
    setup_db()
    app.run(host='0.0.0.0', port=5000)
