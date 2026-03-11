import pytest
from playwright.sync_api import APIRequestContext

pytestmark = pytest.mark.api


def test_create_post_returns_expected_status_and_data(api_context: APIRequestContext):
    new_post = {
        "title": "QA Portfolio Test Post",
        "body": "This is a sample API test payload",
        "userId": 1
    }

    response = api_context.post("/posts", data=new_post)
    response_body = response.json()

    assert response.status == 201
    assert response_body["title"] == new_post["title"]
    assert response_body["body"] == new_post["body"]
    assert response_body["userId"] == new_post["userId"]
    assert "id" in response_body