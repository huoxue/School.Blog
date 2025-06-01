from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os
import math

app = Flask(__name__)

COMMENTS_FILE = 'comments.json'
COMMENTS_PER_PAGE = 10

if not os.path.exists(COMMENTS_FILE):
    with open(COMMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, ensure_ascii=False)

def load_comments():
    with open(COMMENTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_comments(comments):
    with open(COMMENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    page = request.args.get('page', default=1, type=int)
    comments = load_comments()
    total_pages = math.ceil(len(comments) / COMMENTS_PER_PAGE)
    start = (page - 1) * COMMENTS_PER_PAGE
    end = start + COMMENTS_PER_PAGE
    page_comments = comments[start:end]
    return render_template("front.html", comments=page_comments, page=page, total_pages=total_pages)

@app.route("/add_comment", methods=["POST"])
def add_comment():
    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        return jsonify({"success": False, "error": "留言內容不可為空"}), 400

    comments = load_comments()
    new_comment = {
        "text": text,
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    comments.append(new_comment)
    save_comments(comments)
    return jsonify({"success": True, "comment": new_comment})

if __name__ == "__main__":
    app.run(debug=True)

