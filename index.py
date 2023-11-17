from flask import Flask, render_template, request
from datetime import datetime, timezone
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>企管4A 410924535 戴啟原求職資訊</h1>"
    homepage += "<a href=/about>啟原個人簡介</a><br>"
    homepage += "<a href=/company>MIS相關工作介紹</a><br>"
    homepage += "<a href=/mis>興趣合倫碼測驗結果</a><br>"
    homepage += "<a href=/resume>求職履歷自傳</a><br>"
    return homepage



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/company")
def company():
    return render_template("company.html")

@app.route("/mis")
def mis():
    return render_template("mis.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")




if __name__ == "__main__":
    app.run()

