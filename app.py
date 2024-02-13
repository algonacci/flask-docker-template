import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_smorest import Api, Blueprint

import module as md
from auth import auth
from config import CONFIG


def create_app():
    app = Flask(__name__)
    app.config.update(CONFIG)
    CORS(app, resources={
         # update to FE or production link
         r"/*": {"origins": ["http://localhost:3000", "https://example.com"]}
         })
    api = Api(app)
    blp = Blueprint("ML Endpoints",
                    "items",
                    description="Operations on ML model endpoint")

    @blp.route("/")
    def index():
        return jsonify({
            "status": {
                "code": 200,
                "message": "Success fetching the API!"
            }
        }), 200

    @blp.route("/post", methods=["POST"])
    @auth.login_required()
    def post():
        if request.method == "POST":
            input_data = request.get_json()
            return jsonify(input_data), 200
        else:
            return jsonify({"message": "Invalid request method"}), 405

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "status": {
                "code": 400,
                "message": "Client side error!"
            }
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "status": {
                "code": 404,
                "message": "URL not found!"
            }
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "status": {
                "code": 405,
                "message": "Request method not allowed!"
            }
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "status": {"code": 500, "message": "Server error!"}
        }), 500

    api.register_blueprint(blp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
