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

if __name__ == "__main__":
    app.run(debug=True)
