import request


if __name__ == "__main__":
    response = request.get("http://127.0.0.1:5000")
    assert response.status.code == 200
    assert response.json