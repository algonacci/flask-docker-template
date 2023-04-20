import json
import uuid

from dotenv import dotenv_values

from app import app

config = dotenv_values(".env")


def test_index_route():
    response = app.test_client().get("/")
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert type(res) is dict
    assert res["status"]["code"] == 200
    assert res["status"]["message"] == "Success fetching the API!"


def test_post_route_without_authorization():
    payload = {
        "test": "test"
    }
    response = app.test_client().post("/post", json=payload)
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 401
    assert type(res) is dict


def test_post_route_with_authorization():
    payload = {
        "test": "test"
    }
    token = config["SECRET_KEY"]
    response = app.test_client().post("/post",
                                      json=payload,
                                      headers={"Authorization": "Bearer {}".format(token)})
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert type(res) is dict


def test_not_found_route():
    response = app.test_client().get(str(uuid.uuid4()))
    assert response.status_code == 404
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is dict
    assert res["status"]["code"] == 404
    assert res["status"]["message"] == "URL not found!"


def test_method_not_allowed_route():
    response = app.test_client().get("/post")
    assert response.status_code == 405
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is dict
    assert res["status"]["code"] == 405
    assert res["status"]["message"] == "Request method not allowed!"
