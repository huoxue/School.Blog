from flask import Flask, render_template

app = Flask(__name__)

# 部落格文章資料（含新增內容）
posts = [
    {
        "title": "校園簡介",
        "content": """
<p>國立屏東大學創校歷史悠久，前身為屏東師範學院，致力於培養具備專業能力與人文素養的優秀人才。目前擁有三大主要校區，各具特色：</p>

<h3>📍 民生校區</h3>
<ul>
    <li>以教育學院為主，提供完整的師資訓練資源</li>
    <li>設施包含：體育館、游泳池、五育樓、學生宿舍與生活機能區</li>
    <li>特色：二樓有著名的「冰淇淋杓吉祥物」，深受學生喜愛</li>
</ul>

<h3>📍 屏商校區</h3>
<ul>
    <li>以商業與管理學院為主，行政機關多設於此</li>
    <li>設施包含：行政大樓、多功能資源中心、生態池、風雨球場</li>
    <li>特色：擁有綠意盎然的中央草坪與完整體育空間</li>
</ul>

<h3>📍 屏師校區</h3>
<ul>
    <li>以理學院與藝術設計為主，注重科學與創意並重</li>
    <li>設施包含：理工大樓、藝術展演廳、游泳池、實驗室</li>
    <li>特色：圓廳很適合小憩，被學生譽為「最好睡的角落」</li>
</ul>

<h3>📍 龍華校區</h3>
<ul>
    <li>新設立的現代化校區，聚焦智慧科技與數位人文</li>
    <li>設施包含：智慧教室、創客空間、雲端運算中心</li>
    <li>特色：綠建築設計，環保節能</li>
</ul>

<h3>📚 圖書館服務</h3>
<p>全校區皆設有圖書館，提供豐富的紙本與電子資源，並設有安靜自習區與團體討論室。</p>

<p>本校以「誠正仁愛」為校訓，推動多元學習、跨領域合作與國際交流，是南臺灣的重要學術據點。</p>
"""
    },
    {
        "title": "最新活動",
        "content": "下週我們會舉辦園遊會，邀請全校師生參與，共度愉快時光！"
    }
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
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)
