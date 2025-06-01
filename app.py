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
    total_pages = max(1, math.ceil(len(comments) / COMMENTS_PER_PAGE))
    start = (page - 1) * COMMENTS_PER_PAGE
    end = start + COMMENTS_PER_PAGE
    page_comments = comments[start:end]

    # 這裡傳入前端變數，包含分頁留言與其他靜態資料
    return render_template(
        "front.html",
        comments=page_comments,
        page=page,
        total_pages=total_pages,
        news_list=[
            "114學年度第1學期學生選課時程公告",
            "2025第五屆大數據精準行銷盃競賽",
            "★總獎金30萬★屏大2025夏日大進級。酷斯拉自主學習競賽"
        ],
        campus_news_list=[
            "屏東大學與UNISMA合作開設新型專班及雙聯學位",
            "資訊學院深化與朱拉隆功大學的學術合作",
            "屏東大學管理學院與泰國宋卡王子大學簽署合作協議"
        ],
        youtube_embed_url="https://www.youtube.com/embed/eD-yVR6O-nw",
        footer_info=[
            "民生校區：900391 屏東市民生路4-18號",
            "屏商校區：900392 屏東市民生東路51號",
            "屏師校區：900393 屏東市林森路1號",
            "電話：08-7663800　傳真：08-7234406"
        ]
    )

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
