
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_producto(client):
    response = client.get("/producto/1")
    assert response.status_code == 200

def test_post_producto(client):
    response = client.post("/producto", json={"id_producto": 3, "cantidad": 15})
    assert response.status_code == 201

def test_put_producto(client):
    response = client.put("/producto/1", json={"nueva_cantidad": 30})
    assert response.status_code == 200
