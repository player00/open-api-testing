import pytest
from api.posts import Posts
from configuration import API_BASE_URL


@pytest.fixture
def api():
    return Posts(API_BASE_URL)
