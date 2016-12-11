from flask import request, Flask, url_for
from flask_socketio import emit,SocketIO

app = Flask(__name__)

@app.route('/data')
def data() :
	fo = open("data.txt","r+")
	str = fo.read(10);
	return str
	fo.close()
