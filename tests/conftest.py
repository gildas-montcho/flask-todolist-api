import pytest

from src.app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING:True"})
    with app.test_client() as client:
        yield client


@pytest.yield_fixture
def app_client():
    pass
