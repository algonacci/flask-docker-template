from flask_httpauth import HTTPTokenAuth

from config import CONFIG

auth = HTTPTokenAuth(scheme="Bearer")


@auth.error_handler
def unauthorized():
    return {
        "status": {
            "code": 401,
            "msg": "Unauthorized Access!"
        }
    }, 401


@auth.verify_token
def verify_token(token):
    return CONFIG['SECRET_KEY'] == token
