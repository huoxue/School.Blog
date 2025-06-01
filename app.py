from flask import Flask, render_template

app = Flask(__name__)

from data import posts

@app.route("/")
def index():
    return render_template("front.html")

@app.route("/about")
def about():
    return render_template("about.html", posts=posts)
    
@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html", post=posts[post_id])

@app.route("/map")
def map():
    return render_template("map.html")
    
@app.route("/admission")
def admission():
    return "<h1>招生資訊頁面尚在建置中</h1>"

@app.route("/academics")
def academics():
    return "<h1>學術單位頁面尚在建置中</h1>"

@app.route("/administration")
def administration():
    return "<h1>行政單位頁面尚在建置中</h1>"

@app.route("/library")
def library():
    return "<h1>圖書館頁面尚在建置中</h1>"
if __name__ == "__main__":
    app.run(debug=True)
