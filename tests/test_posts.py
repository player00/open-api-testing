import pytest
import allure


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
    payload = {
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1
    }
    response = api.create_post(payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]
    assert response.json()["body"] == payload["body"]
    assert response.json()["userId"] == payload["userId"]


@allure.feature("Posts")
@allure.story("Update a Post")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_post(api):
    post_id = 1
    payload = {
        "id": post_id,
        "title": "Updated Test Post",
        "body": "This is an updated test post",
        "userId": 1
    }
    response = api.update_post(post_id, payload)
    assert response.status_code == 200
    assert response.json()["id"] == post_id
    assert response.json()["title"] == payload["title"]
    assert response.json()["body"] == payload["body"]
    assert response.json()["userId"] == payload["userId"]


@allure.feature("Posts")
@allure.story("Partially Update a Post")
@allure.severity(allure.severity_level.NORMAL)
def test_partial_update_post(api):
    post_id = 1
    payload = {
        "title": "Partially Updated Test Post"
    }
    response = api.partial_update_post(post_id, payload)
    assert response.status_code == 200
    assert response.json()["id"] == post_id
    assert response.json()["title"] == payload["title"]


@allure.feature("Posts")
@allure.story("Delete a Post")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_post(api):
    post_id = 1
    response = api.delete_post(post_id)
    assert response.status_code == 200
