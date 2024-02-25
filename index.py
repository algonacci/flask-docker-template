from flask_smorest import Blueprint
from flask import jsonify, request
from auth import auth
from cache import cache
from rate_limiter import limiter


bp = Blueprint("index",
               "items",
               description="Operations on ML model endpoint")


@bp.route("/")
@limiter.limit("5 per day")
@cache.cached(timeout=60)
def index():
    return jsonify({
        "status": {
            "code": 200,
            "message": "Success fetching the API!"
        },
        "data": None
    }), 200


@bp.route("/post", methods=["POST"])
@auth.login_required()
def post():
    if request.method == "POST":
        input_data = request.get_json()
        return jsonify(input_data), 200
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Invalid request method",
            },
            "data": None,
        }), 405
