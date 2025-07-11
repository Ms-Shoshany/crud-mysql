from flask import Flask, request, jsonify
from flask_cors import CORS
from endpoints import object_page

app = Flask(__name__)

app.register_blueprint(object_page)

CORS(app, supports_credentials=True)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)