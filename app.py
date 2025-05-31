from flask import Flask, render_template

app = Flask(__name__)

# 假設部落格文章資料
posts = [
    {"title": "校園簡介", "content": "我們的學校創立於..."},
    {"title": "最新活動", "content": "下週我們會舉辦園遊會..."},
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", post=posts[post_id])

@app.route("/map")
def map():
    return render_template("map.html")  # ✅ 必須寫在 run() 之前

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)


