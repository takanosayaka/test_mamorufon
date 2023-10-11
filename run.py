# ライブラリのインポート
from flask import Flask, render_template
from flask_socketio import SocketIO

# インスタンスを作成
app = Flask(__name__)
socketio = SocketIO(app)

from view1 import site1_bp
app.register_blueprint(site1_bp)

from view2 import site2_bp
app.register_blueprint(site2_bp)

# HTMLページに対するルーティング
@app.route('/')
def home():
  return render_template('home.html')

# 訪問ボタン押下時に実行
@socketio.on('visit_message')
def visit_recept(data):
  visit_message = data["message"]
  # クライアント（インターフォン）に対してイベントを送る
  socketio.emit('receive_visit', {'message': visit_message})

# 会話ボタン押下時に実行
@socketio.on('speak_start')
def speak_recept(data):
  speak_message = data["message"]
  # クライアントに対してイベントを送る
  socketio.emit('speak_message', {'message': speak_message})

if __name__ == '__main__':
  socketio.run(app, port=8080)