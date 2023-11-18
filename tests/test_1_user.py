import sys
sys.path.append(".")
from main import app

def test_create_user_api():
    response = app.test_client().post("/user", json={
        "name": "huzaifa",
        "email": "huzaifa@gmail.com",
        "password": "123456"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert data["data"]["id"] > 0

def test_create_user_api_without_required_data():
    response = app.test_client().post("/user", json={
        "name": "hello"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert "error" in data
    assert "message" in data["error"]
    assert data["error"]["message"].endswith("field is required")

def test_login_user_api():
    response = app.test_client().post("/login", json={
        "email": "huzaifa@gmail.com",
        "password": "123456"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["message"] == "user login successfully"
    assert "token" in data

def test_login_user_api_without_required_data():
    response = app.test_client().post("/login", json={
        # "email": "huzaifa13@gmail.com"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert "error" in data
    assert "message" in data["error"]
    assert data["error"]["message"].endswith("field is required")

def test_login_user_with_wrong_credential():
    response = app.test_client().post("/login", json={
        "email": "fake",
        "password": "fake"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data == {'error': {'message': 'invalid email or password'}}
