from flask import Flask
from flask_socketio import SocketIO
from eventlet import monkey_patch
import redis

monkey_patch()

app = Flask(__name__)
app.secret_key = 'strong_secret_key_here!'
app.config['DEBUG'] = True
socket = SocketIO(app, async_mode='eventlet')
r_cli = redis.StrictRedis(host='127.0.0.1', port=6379, db=1, decode_responses=False)

from app import routes