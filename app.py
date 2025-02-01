from flask import Flask, jsonify, render_template
from flask_cors import CORS  # 解決跨域問題
from flask_sqlalchemy import SQLAlchemy
from models import db, User, get_all_users

app = Flask(__name__)
CORS(app)  # 允許所有域訪問（僅供開發測試用）
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mypgsql_4kto_user:CDDkZiGqv6L2GSt5GxfKbjHW2jOkQPnB@dpg-cuf1ghggph6c73foumng-a/mypgsql_4kto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化DB
db.init_app(app)

# 创建数据库表
with app.app_context():
    db.create_all()
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    users = get_all_users()  # 调用 models.py 中的函数
    return f"Users: {users}"

@app.route('/api/users')
def users():
    new_user = User(username='testuser', email='test@example.com')
    db.session.add(new_user)
    db.session.commit()

    users = User.query.all()
    print(users)
    return jsonify([{"username": user.username, "email": user.email} for user in users])

if __name__ == '__main__':
    app.run(debug=True)