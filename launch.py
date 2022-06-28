# launcher.py
from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify(result="hello!")
if __name__ == "__main__":
    # "0,0,0,0" 부분을 생략하시면 기본으로 localhost가 세팅됩니다.
    app.run("0.0.0.0", port=5000)  # 0.0.0.0 : 모든 도메인을 허용