import pytest
from api.posts_api import PostsApi
from configuration import API_BASE_URL


@pytest.fixture
def api():
    return PostsApi(API_BASE_URL)
