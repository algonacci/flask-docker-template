import json
import uuid
import pytest
from dotenv import dotenv_values
from app import create_app

config = dotenv_values(".env")


@pytest.fixture
def app():
    app = create_app()
    yield app


def test_index_route(app):
    response = app.test_client().get("/")
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert type(res) is dict
    assert res["status"]["code"] == 200
    assert res["status"]["message"] == "Success fetching the API!"
    assert res["data"] == None


def test_post_route_without_authorization(app):
    payload = {"test": "test"}
    response = app.test_client().post("/post", json=payload)
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 401
    assert type(res) is dict


def test_post_route_with_authorization(app):
    payload = {"test": "test"}
    token = config["SECRET_KEY"]
    response = app.test_client().post("/post",
                                      json=payload,
                                      headers={"Authorization": "Bearer {}".format(token)})
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert type(res) is dict


def test_not_found_route(app):
    response = app.test_client().get(str(uuid.uuid4()))
    assert response.status_code == 404
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is dict
    assert res["status"]["code"] == 404
    assert res["status"]["message"] == "URL not found!"
    assert res["data"] == None


def test_method_not_allowed_route(app):
    response = app.test_client().get("/post")
    assert response.status_code == 405
    res = json.loads(response.data.decode('utf-8'))
    assert type(res) is dict
    assert res["status"]["code"] == 405
    assert res["status"]["message"] == "Request method not allowed!"
    assert res["data"] == None
