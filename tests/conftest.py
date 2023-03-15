import pytest
from api.posts_api import PostsAPI
from configuration import API_BASE_URL


@pytest.fixture
def api():
    return PostsAPI(API_BASE_URL)
