from flask import Flask, jsonify
from flask_cors import CORS  # 解決跨域問題

app = Flask(__name__)
CORS(app)  # 允許所有域訪問（僅供開發測試用）

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)