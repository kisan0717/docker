from flask import Flask, request, jsonify
from business import get_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def hello_world():
    
    return 'Hello, world!'

@app.route('/api', methods=['GET'])
def api():
    
    data = get_data()
    
    data = {
		'data': data
	}
    
    return jsonify(data)

if __name__ == '__main__':
    
	app.run(port=8000, host='0.0.0.0', debug=True)