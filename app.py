from flask import Flask, jsonify, render_template
from crawler import fetch_exchange_rates  # 假設上面程式存在 crawler.py

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/rate")
def api_rate():
    rates = fetch_exchange_rates()
    return jsonify(rates)

if __name__ == "__main__":
    # localhost = 172.20.10.2
    app.run(host='0.0.0.0', port=5000, debug=True) # 正式使用必須要關掉debug，否則別人可以訪問伺服器
    