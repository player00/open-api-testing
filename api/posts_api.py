from .requests_wrapper import RequestsWrapper


class PostsAPI(RequestsWrapper):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_all_posts(self):
        return self.get("posts")

    def get_post_by_id(self, post_id):
        return self.get(f"posts/{post_id}")

    def create_post(self, payload):
        return self.post("posts", payload)

    def update_post(self, post_id, payload):
        return self.put(f"posts/{post_id}", payload)

    def partial_update_post(self, post_id, payload):
        return self.patch(f"posts/{post_id}", payload)

    def delete_post(self, post_id):
        return self.delete(f"posts/{post_id}")
