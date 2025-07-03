from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_status():
    client = app.test_client()
    response = client.get('/status')
    assert response.status_code == 200
    assert response.json == {"status": "OK"}
<<<<<<< HEAD


def test_metrics():
    client = app.test_client()
    response = client.get('/metrics')
    assert response.status_code == 200
=======
>>>>>>> 7d693a82924c567a74d8690d228ccbdc44a8f313
