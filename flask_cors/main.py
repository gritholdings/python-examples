from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import os

class Server:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)  # Enable CORS for all routes
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/data', methods=['POST'])
        def receive_data():
            data = request.json
            if not data:
                logging.error('No JSON received')
                return jsonify({"status": "error", "message": "No JSON received"}), 400

            method = data.get('method')
            text_input = data.get('text_input')
            if method == 'uppercase':
                try:
                    result = text_input.upper()
                    return jsonify({"status": "success", "result": result}), 200
                except Exception as e:
                    logging.error(f"Error processing request: {e}")
                    return jsonify({"status": "error", "message": "Internal server error"}), 500
            elif method == 'lowercase':
                try:
                    result = text_input.lower()
                    return jsonify({"status": "success", "result": result}), 200
                except Exception as e:
                    logging.error(f"Error processing request: {e}")
                    return jsonify({"status": "error", "message": "Internal server error"}), 500
            else:
                logging.error('Invalid method')
                return jsonify({"status": "error", "message": "Invalid method"}), 400

        @self.app.route('/')
        def index():
            return 'Index Page'

    def run(self):
        port = int(os.getenv('PORT', 5000))
        self.app.run(debug=False, port=port)

if __name__ == '__main__':
    server = Server()
    server.run()
