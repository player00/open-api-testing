import allure
from models.post import Post


@allure.feature("Posts")
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_posts(api):
    response = api.get_all_posts()
    assert response.status_code == 200
    assert len(response.json()) == 100


@allure.feature("Posts")
@allure.story("Get Post by ID")
@allure.severity(allure.severity_level.NORMAL)
def test_get_post_by_id(api):
    post_id = 1
    response = api.get_post_by_id(post_id)
    assert response.status_code == 200
    assert response.json()["id"] == post_id


@allure.feature("Posts")
@allure.story("Create a Post")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_post(api):
    new_post = Post(title="New post title", body="New post body", userId=1)
    response = api.create_post(new_post)

    assert response.status_code == 201
    created_post = response.json()
    assert created_post["title"] == new_post.title
    assert created_post["body"] == new_post.body
    assert created_post["userId"] == new_post.userId


@allure.feature("Posts")
@allure.story("Update a Post")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_post(api):
    post_id = 1
    updated_post = Post(
        id=post_id,
        title="Updated Test Post",
        body="This is an updated test post",
        userId=1
    )
    response = api.update_post(post_id, updated_post)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == post_id
    assert response_data["title"] == updated_post.title
    assert response_data["body"] == updated_post.body
    assert response_data["userId"] == updated_post.userId


@allure.feature("Posts")
@allure.story("Partially Update a Post")
@allure.severity(allure.severity_level.NORMAL)
def test_partial_update_post(api):
    post_id = 1
    payload = {
        "title": "Partially Updated Test Post"
    }
    response = api.update_post(post_id, payload)
    assert response.status_code == 200
    assert response.json()["id"] == post_id
    assert response.json()["title"] == payload["title"]


@allure.feature("Posts")
@allure.story("Delete a Post")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_post(api):
    post_to_delete = api.create_post(
        Post(title="Post to delete", body="This post will be deleted", userId=1)).json()
    delete_response = api.delete_post(post_to_delete["id"])

    assert delete_response.status_code == 200
    get_response = api.get_post_by_id(post_to_delete["id"])
    assert get_response.status_code == 404
