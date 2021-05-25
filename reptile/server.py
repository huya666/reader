from flask import Flask
import json
# from gevent.pywsgi import WSGIServer
from start import search

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
	result = search.searchList('完美世界')
	return result

@app.route('/api', methods=['GET'])
def index():
  return "Hello, World!"

if __name__ == '__main__':
	# Debug/Development
	app.run(debug=False, host="0.0.0.0", port="5000")
	# Production
	# http_server = WSGIServer(('', 5000), app)
	# http_server.serve_forever()