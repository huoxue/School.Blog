from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
COMMENTS_FILE = 'comments.json'

def load_comments():
    if os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_comments(comments):
    with open(COMMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

@app.route('/')
def front_page():
    return render_template('front.html')

@app.route('/get_comments')
def get_comments():
    return jsonify(load_comments())

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.json.get('comment')
    if comment:
        comments = load_comments()
        comments.insert(0, {"text": comment})
        save_comments(comments)
        return jsonify(success=True)
    return jsonify(success=False), 400

if __name__ == '__main__':
    app.run(debug=True)
