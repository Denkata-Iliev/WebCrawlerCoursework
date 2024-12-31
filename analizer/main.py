from nltk.sentiment.vader import SentimentIntensityAnalyzer  # type: ignore
from flask import Flask, jsonify  # type: ignore
from flask_socketio import SocketIO  # type: ignore
import utils
import json

app = Flask(__name__)
socketio = SocketIO(app)

class AnalizedPost:
    def __init__(self, url, content, compound, negative, neutral, positive):
        self.url = url;
        self.content = content;
        self.compound = compound;
        self.negative = negative;
        self.neutral = neutral;
        self.positive = positive;


def analize(posts):
    analizedRecords = []
    for post in posts:
        sid = SentimentIntensityAnalyzer()
        
        sentiment_scores = sid.polarity_scores(post.content)
            
        analizedRecords.append(
            AnalizedPost(
                post.url,
                post.content,
                sentiment_scores['compound'],
                sentiment_scores['neg'],
                sentiment_scores['neu'],
                sentiment_scores['pos']
            )
        )
        
    return analizedRecords


@app.route('/new-data-ready', methods=['POST'])
def new_data_ready():
    posts = utils.get_all_last_mins(2)
    analizedPosts = analize(posts)
    
    for post in analizedPosts:
        utils.save_in_db(post)

    toBeSerialized = [item.__dict__ for item in analizedPosts]
    socketio.emit('message', json.dumps(toBeSerialized))

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    utils.setup_db()
    socketio.run(app, host="0.0.0.0", port="5001")