from flask import request, Flask, url_for
from flask_socketio import emit,SocketIO

app = Flask(__name__)

@app.route('/data')
def data() :
	fo = open("data.txt","r+")
	raw_data = fo.read(10);
	fo.close()
	return raw_data
