# from tests.conftest import client


from src.constants import HEALTH_MSG


def test_should_status_code_200_ok(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_should_return_health_msg(client):
    response = client.get("/health")
    data = response.data.decode()
    assert data == HEALTH_MSG
