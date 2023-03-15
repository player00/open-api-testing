from models.post import Post
from .requests_wrapper import ApiClient
from requests import Response
from dataclasses import asdict


class Posts(ApiClient):
    def __init__(self, base_url: str):
        super().__init__(base_url)
        self.posts_url = "posts"

    def get_post_by_id(self, post_id: int) -> Response:
        return self.get(f"{self.posts_url}/{post_id}")

    def create_post(self, post: Post) -> Response:
        return self.post(self.posts_url, asdict(post))

    def update_post(self, post_id: int, *args) -> Response:
        if type(args[0]) == Post:
            return self.put(f"{self.posts_url}/{post_id}", asdict(args[0]))
        elif type(args[0]) == dict:
            return self.patch(f"{self.posts_url}/{post_id}", args[0])

    def delete_post(self, post_id: int) -> Response:
        return self.delete(f"{self.posts_url}/{post_id}")

    def get_all_posts(self) -> Response:
        return self.get(self.posts_url)
