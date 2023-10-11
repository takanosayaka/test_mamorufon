# ライブラリのインポート
from flask import Flask, render_template
from flask_socketio import SocketIO

# インスタンスを作成
app = Flask(__name__)
socketio = SocketIO(app)

from view_intercom import intercom_bp
app.register_blueprint(intercom_bp)

from view_monitor import monitor_bp
app.register_blueprint(monitor_bp)

# HTMLページに対するルーティング
@app.route('/')
def home():
  return render_template('home.html')

# 訪問ボタン押下時に実行
@socketio.on('visit_message')
def visit_recept(data):
  visit_message = data["message"]
  # モニターに対してイベントを送る
  socketio.emit('receive_visit_message', {'message': visit_message})

# 会話ボタン押下時に実行
@socketio.on('response_message')
def response_recept(data):
  resident_message = data["message"]
  # インターフォンに対してイベントを送る
  socketio.emit('recieve_resident_message', {'message': resident_message})

if __name__ == '__main__':
  socketio.run(app, port=8080)