from flask import Flask, jsonify, render_template, request
from flask_cors import CORS  # 解決跨域問題

app = Flask(__name__)
CORS(app)  # 允許所有域訪問（僅供開發測試用）

# 初始化DB


# 创建数据库表

    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flaskkk!"})

if __name__ == '__main__':
    app.run(debug=True)