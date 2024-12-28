from flask import Flask, request, jsonify  # type: ignore
from utils import fetch_content


def save_in_db(parsed_data):
    print(parsed_data)

app = Flask(__name__)

@app.route('/submit-urls', methods=['POST'])
def submit_urls():
    urls = request.json.get('urls', [])
    
    # scrape given urls
    for url in urls:
        parsed_data = fetch_content(url)
        save_in_db(parsed_data)
    
    print(f"Received URLs: {urls}")
    return jsonify({"status": "success", "message": f"Received {len(urls)} URLs"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)